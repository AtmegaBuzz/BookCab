import googlemaps
import math
import pymysql
import os

from itertools import permutations
from BookCab.models import (
    Booking,
    Source
)

from decouple import config

print(config("google_api_key","dasdasd"),"=====")
gmaps = googlemaps.Client(key=config("google_api_key","dasdasd"))



def get_distance(src, dest):
    
    if src + dest in distance_matrix_map:
        return distance_matrix_map[src + dest]
    else :
        my_dist = gmaps.distance_matrix(src, dest)['rows'][0]['elements'][0]
        # print(src + " " + dest)
        # print(my_dist["status"])
        if my_dist["status"]=="OK":
            distance_matrix_map[src + dest] = my_dist['distance']['value']
            distance_matrix_map[dest + src] = my_dist['distance']['value']
            time_matrix_map[src + dest] = my_dist['duration']['value']
            time_matrix_map[dest + src] = my_dist['duration']['value']
            return distance_matrix_map[src + dest]
        
        return None

def get_duration(src, dest) :
    if (src + dest) in time_matrix_map:
        return time_matrix_map[src + dest]
    else :
        my_dist = gmaps.distance_matrix(src, dest)['rows'][0]['elements'][0]
        distance_matrix_map[src + dest] = my_dist['distance']['value']
        distance_matrix_map[dest + src] = my_dist['distance']['value']
        time_matrix_map[src + dest] = my_dist['duration']['value']
        time_matrix_map[dest + src] = my_dist['duration']['value']
        return time_matrix_map[src + dest]




def get_cost(duration,distance,milage,min_cost=50,seater=4):
    
    fuel_price = 0
    
    fuel_to_burn = distance/milage
    base_cost = (fuel_to_burn*fuel_price) + min_cost
    additional_cost = (base_cost/100)*seater # seater cost
    gst = ((base_cost+additional_cost)/100)*18 # 18 % gst
    
    total_cost =  base_cost+additional_cost+gst
    
    return total_cost
    
    
    
    




def databaseConnect():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='admin',
                                 db='btp',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection




distance_matrix_map = dict()
time_matrix_map = dict()



class dpstate:
    def __init__(self, taxino, curloc, curtime, users_in_taxi):
        self.taxino = taxino
        self.curloc = curloc
        self.curtime = curtime
        self.users_in_taxi = users_in_taxi

    def __hash__(self):
        val = 0
        for i in self.users_in_taxi:
            val += i * i
        return hash((self.taxino, self.curloc, self.curtime)) + val

    def __eq__(self, other):
        return (self.taxino, self.curloc, self.curtime, self.users_in_taxi) == (other.taxino, other.curloc, other.curtime, other.users_in_taxi)

    def to_string(self):
        return self.taxino + " " + self.curloc + " " + self.curtime + " " + self.users_in_taxi


class User:

    def __init__(self, id, destination,booking_id):
        self.id = id
        self.destination = destination
        self.booking_id = booking_id
        
    def to_string(self):
        return self.id + " " + self.destination


class UserAttributes:

    def __init__(self, userid, destination, booking_id ,distance, time, cost):
        self.userid = userid
        self.destination = destination
        self.booking_id = booking_id
        self.distance = distance
        self.time = time
        self.cost = cost

    def to_string(self):
        return str(self.userid) + " " + self.destination + " " + str(self.distance) + " " + str(self.time) + " " + str(self.cost)



cache = dict()
users = list()
groups = list()
n = 0
answer = 1e9
home_source = Source.objects.values_list(
    "location_name"
    ).all().first()[0]


# set default root location
if not home_source:
    source = 'rajiv chowk'

def solve(taxino, curloc, curtime, users_in_taxi, cost, best_config):

    global answer
    if users_in_taxi.count(0) + users_in_taxi.count(1) == 0:
        if cost < answer:
            best_config.clear()
            for i in users_in_taxi:
                best_config.append(i)
            answer = cost
        return 0
    if dpstate(taxino, curloc, curtime, users_in_taxi) in cache:
       return cache[dpstate(taxino, curloc, curtime, users_in_taxi)]

    res = 1e9

    # Move on to new taxi if all passengers have reached their destination
    if curloc != home_source and users_in_taxi.count(1) == 0:
        return solve(taxino + 1, home_source, 0, users_in_taxi, cost, best_config)

    # Try picking up passengers if there is space and we are at source and calculate best result
    picked_up = users_in_taxi.count(1)
    for i in range(0, n):

        if picked_up < 4 and users_in_taxi[i] == 0 and curloc == home_source:
            users_in_taxi[i] = 1
            res = min(res, solve(taxino, curloc, curtime, users_in_taxi, cost, best_config))
            users_in_taxi[i] = 0

    # Try dropping off passengers and see if it yields best result
    for i in range(0, n) :

        if users_in_taxi[i] == 1:
            users_in_taxi[i] = taxino
            res = min(res, get_distance(curloc, users[i].destination) + solve(taxino, users[i].destination, curtime + get_distance(curloc, users[i].destination), users_in_taxi, cost + get_distance(curloc, users[i].destination), best_config))
            users_in_taxi[i] = 1

    cache[dpstate(taxino, curloc, curtime, users_in_taxi)] = res
    
    return res


def cost_calculator(dist, tot_dist, min_cost, tot_cost) :
    val = (1.0 * dist) / (1.0 * tot_dist)
    val *= tot_cost
    val = math.floor(val)
    val = max(val, min_cost)
    return val/10


def print_group_pattern(users_in_taxi) :
    users_done = 0

    try:
        for i in range(2, 1000):
            if users_done >= n:
                return

            
            cur_cab_users = list()
            print("Taxi #" + str(i - 1) + ": ")
            for j in range(0, n):
                if users_in_taxi[j] == i:
                    print(str(users[j].id) + " ")
                    users_done += 1
                    cur_cab_users.append(users[j])
            print("")
            # Process current cab users to form person attribute object for each of the user sitting in this cab
            tot_users = len(cur_cab_users)
            if tot_users == 0 :
                return
            # Groups is a list which is the final object to be sent to front end and comprises of a list of "group" and each "group" is a list of "UserAttributes"
            # We are here to find current group details
            group = list()
            perm = list()
            for x in range(0, tot_users):
                perm.append(x)
            perm_list = permutations(perm)

            min_dist = 1e9
            for candidate in perm_list:
                cur_dist = get_distance(home_source, cur_cab_users[candidate[0]].destination)
                for idx in range(1, tot_users):
                    cur_dist += get_distance(cur_cab_users[candidate[idx - 1]].destination, cur_cab_users[candidate[idx]].destination)

                if(cur_dist > min_dist):
                    continue
                # Update the best group
                print(candidate)
                group.clear()
                min_dist = cur_dist
                dur_so_far = get_duration(home_source, cur_cab_users[candidate[0]].destination)
                dist_so_far = get_distance(home_source, cur_cab_users[candidate[0]].destination)
                minimum_cost = 53
                total_cost = 60 + 12 * ((1.0 * cur_dist)/ (1000.0))

                group.append(UserAttributes(cur_cab_users[candidate[0]].id, cur_cab_users[candidate[0]].destination,cur_cab_users[candidate[0]].booking_id,
                                            dist_so_far, dur_so_far, cost_calculator(dist_so_far, cur_dist, minimum_cost, total_cost)))

                for idx in range(1, tot_users):
                    dur_so_far += get_duration(cur_cab_users[candidate[idx - 1]].destination, cur_cab_users[candidate[idx]].destination)
                    dist_so_far = get_distance(cur_cab_users[candidate[idx - 1]].destination, cur_cab_users[candidate[idx]].destination)

                    group.append(UserAttributes(cur_cab_users[candidate[idx]].id, cur_cab_users[candidate[idx]].destination,cur_cab_users[candidate[idx]].booking_id,
                                                dist_so_far, dur_so_far,cost_calculator(dist_so_far, cur_dist, minimum_cost, total_cost)))
            
            groups.append(group)
            
    except:
        print("")
        

def populate_user_list(bookings) :
    users = list()
    
    try:

        for booking in bookings:
            user_id = booking.user.id
            dest = booking.destination
            booking_id = booking.id
            print(booking_id,"booking")
            users.append(User(user_id, dest,booking_id))
           
    except Exception as e:
        print("err",e)
        
    return users


def main():

    global n
    global users
    global groups
   
    bookings = Booking.objects.all().filter(status=0)
    users = populate_user_list(bookings)
    n = len(users)
    users_in_taxi = [0 for i in range(n)]
    best_config = list()
    mincost = solve(2, home_source, 0, users_in_taxi, 0, best_config)

    print_group_pattern(best_config)


    return groups
        
    
            
    

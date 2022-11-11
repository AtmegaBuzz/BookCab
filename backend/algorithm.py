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
    pass

class User:

    pass


class UserAttributes:
    pass

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
    pass


def cost_calculator(dist, tot_dist, min_cost, tot_cost) :
    pass


def print_group_pattern(users_in_taxi) :
    pass
        

def populate_user_list(bookings) :
    pass

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
        
    
            
    

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

gmaps = googlemaps.Client(key=config("google_api_key","dasdasd"))



def get_distance(src, dest):
    
    pass
        
        return None

def get_duration(src, dest) :
    pass




def get_cost(duration,distance,milage,min_cost=50,seater=4):
    
    pass
    
    
    
    




def databaseConnect():
    pass




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
        
    
            
    

<p><img src="https://raw.githubusercontent.com/AtmegaBuzz/osmd/main/screenshots/logo.jpeg" alt="logo" width="20%" /></p>

# OSMD Book Cab (One Source Multiple Destination)

- [About Project](#About-Project)

- [Working](#Working)
  - [Login](#Login)
  - [Booking Cab](#Booking-Cab)
  - [Your Bookings](#Your-Bookings)
  - [Accepted Bookings](#Bookings-Accepted)
  - [Individual Bookings](#Individual-Bookings)
  - [Chat Functionality](#Chats)

- [Getting Started](#Getting-Started)
  - [How to Add Google Maps Api](#oogle-api)
  - [How to Add Redis Host](#redis-host)
  - [Setup And Run the Application](#run)

<a id="About-Project"></a>

# About OSMD Book Cab

- Book Cab is a web app that optimizes the rideshare booking approach. This app serves as a single source to help users find the shortest path for multiple destination, shared rides.

- The goal of this project is to figure out the shortest feasible path from a given starting point using an algorithm. The performance of the developed algorithm will be studied for practical use.


# How it Works
- Works on Bellman-Ford algorithm to compute shortest and optimized  path by considering each location as a vertex of the graph.
- The booking is then paired with max 4 people based on the route and low cost.

### What is Bellman-Ford Algorithm 
The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.

## Features and Interfaces

1. Registration page <a id="Login"></a>
   - ![image](https://user-images.githubusercontent.com/68425016/152768563-2832bac6-9097-4ddc-986d-0df97379b1cd.png)

2. Booking page <a id="Booking-Cab"></a>
   - ![image](https://user-images.githubusercontent.com/68425016/152768627-17fb7908-3da2-421c-ad3c-7298d8b4b55a.png)

3. Your bookings  <a id="Your-Bookings"></a>
   - ![image](https://user-images.githubusercontent.com/68425016/152768780-d900ff3b-6d50-40f2-9f63-57a98df07017.png)

4. Bookings accepted <a id="Bookings-Accepted"></a>
	- Booking accepted but payment pending 
   - ![image](https://user-images.githubusercontent.com/68425016/207077739-6405d320-1edf-45d6-b92d-3cae063f4176.png)
	- paying using ethereum (SepoliaETH)
   - ![image](https://user-images.githubusercontent.com/68425016/207078028-ed56e3ee-0c54-414d-9211-11d2e2fc7db5.png)


5. Bookings accepted <a id="Individual-Bookings"></a>
	- Booking info of individuals who will be sitting in the same shared cab. 
   - ![image](https://user-images.githubusercontent.com/68425016/152769026-09d94746-f7d9-4d7b-9852-8ffad5331587.png)

5. Your route <a id="Individual-Bookings"></a>
	- See your route on your bookings accepted page. 
   - ![image](https://user-images.githubusercontent.com/68425016/201683649-67dd6a5c-d217-4a90-983c-fd265760774a.png)

  
6. Chat Functionality <a id="Chats"></a>
   - ![image](https://user-images.githubusercontent.com/68425016/201581222-b6841c98-1001-47d7-bfbe-d82e33eca63b.png)


<a id="Getting-Started"></a>

## Getting Started

<a id="google-api"></a>

- #### Add google maps API.

 	- Create your billing account at [google maps platform](https://mapsplatform.google.com/) (google console).
	 - Generate Api key to access the services.
 	- Add the api to .env file. 

<a id="run"></a>

- #### Setup using docker
	- ````docker-compose build````
	- ````docker-compose up````


- #### Setup
	 - ```pip install -r requirements.txt``` 
	 - ```python server.py```

- #### Run Tests using pytest
	- ```pip install pytest```
	- ```python -m pytest```

test

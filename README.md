
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

# OSMD Cab Infrastructure

One Source, Multiple Destination Book Cab App, is a cab app Website that focuses on optimizing the approach of booking shared from a single source.

We target organizations such as large MNC offices, Schools, or prominent gathering places, which are handled by an organization that has many individuals and wants to implement their own cab services.

This Idea focuses on providing the common Open-Source Infrastructure to the Organizations to implement their own software in delivering the cab services. 

<a id="Working"></a>

# How it Works
```This Algorithm for this app is created by NSIT Last year student colaborated with Swapnil Shinde for Implementation. Last year project NSIT```
1.It Is based on Bellman Ford algorith for shortest path | One source Multiple destination.
2.This app takes the Const Starting point which will be same for all users , it can be a organisation or a school.
3.then it optimises the path for one source to multiple destination

<a id="Login"></a>

# Login
![DeepinScreenshot_select-area_20220207153128](https://user-images.githubusercontent.com/68425016/152768563-2832bac6-9097-4ddc-986d-0df97379b1cd.png)

<a id="Booking-Cab"></a>

# Booking Cab
![DeepinScreenshot_select-area_20220207153250](https://user-images.githubusercontent.com/68425016/152768627-17fb7908-3da2-421c-ad3c-7298d8b4b55a.png)

<a id="Your-Bookings"></a>

# Your Bookings 
![DeepinScreenshot_select-area_20220207153341](https://user-images.githubusercontent.com/68425016/152768780-d900ff3b-6d50-40f2-9f63-57a98df07017.png)

<a id="Bookings-Accepted"></a>

# Bookings accepted 
![DeepinScreenshot_select-area_20220207153528](https://user-images.githubusercontent.com/68425016/152768864-d36cdfc0-e45b-4d48-8965-b66697a478c4.png)

<a id="Individual-Bookings"></a>

# Individual Bookings Info (info of people who will be sitting on same shared cab).
![DeepinScreenshot_select-area_20220207153552](https://user-images.githubusercontent.com/68425016/152769026-09d94746-f7d9-4d7b-9852-8ffad5331587.png)

<a id="Chats"></a>

# Chat Functionality.
![DeepinScreenshot_select-area_20220207153749](https://user-images.githubusercontent.com/68425016/152769124-3713e000-bbe8-46b9-a6a3-2d3c3017045d.png)


<a id="Getting-Started"></a>

## Getting Started

<a id="google-api"></a>

#### Add google maps API.

 - go to google developer console and enable and generate your own Google Maps Api
 - add the api to .env file. 

<a id="redis-host"></a>

#### Add Redis Host URI. 
 - go to redis lab and setup your own redis database 
 - add the redis host uri to .env 

<a id="run"></a>

#### Setup and Run the Application
 - ```pip install requirements.txt``` 
 - ```python manage.py makemigrations```
 - ```python manage.py migrate```
 - ```python manage.py runserver```


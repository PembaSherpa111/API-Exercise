from dataclasses import dataclass
import datetime
import requests
import csv

@dataclass
class Film:
    title : str
    director : str
    producer : str
    release_date : datetime.date
    running_time : int

@dataclass
class People(Film):
    name : str
    gender : str
    eye_color : str
    hair_color : str

@dataclass
class Species(People):
    classification : str

@dataclass
class Location(Film):
    name : str
    climate : str
    terrain : str

@dataclass
class Vehicle(Film):
    name : str
    vehicle_class : str
    length : str

#grabbing film data
film_data = requests.get("https://ghibliapi.herokuapp.com/films/")
film_list = film_data.json()
films=[]
for i in range(0,len(film_list)):
    film = Film(film_list[i]["title"],film_list[i]["director"],film_list[i]["producer"],film_list[i]["release_date"],film_list[i]["running_time"])
    films.append(film)

print(films)



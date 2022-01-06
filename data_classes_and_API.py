from dataclasses import dataclass
import datetime

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

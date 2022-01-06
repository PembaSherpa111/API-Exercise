from dataclasses import dataclass
import datetime
import requests

@dataclass
class Film:
    filmID : str
    title : str
    director : str
    producer : str
    release_date : datetime.date
    running_time : int

@dataclass
class Species():
    speciesID: str
    classification : str
    eye_color : str
    hair_color : str
    filmID : list

@dataclass
class People():
    name : str
    gender : str
    eye_color : str
    hair_color : str
    filmID : str
    speciesID : str

@dataclass
class Location():
    name : str
    climate : str
    terrain : str
    filmID : str

@dataclass
class Vehicle():
    name : str
    vehicle_class : str
    length : str
    filmID : str

# Function to grab list of film ID from film API url. Note : the film url must be list and not string data type
def get_filmID(film_url):
    filmID = []
    for x in range(0,len(film_url)):
        data = requests.get(f"{film_url[x]}")
        list = data.json()
        filmID.append(list["id"])
    return filmID


#grabbing film data
film_data = requests.get("https://ghibliapi.herokuapp.com/films/")
film_list = film_data.json()
films=[]
for i in range(0,len(film_list)):
    film = Film(film_list[i]["id"],film_list[i]["title"],film_list[i]["director"],film_list[i]["producer"],film_list[i]["release_date"],film_list[i]["running_time"])
    films.append(film)

#grabbing species data
species_data = requests.get("https://ghibliapi.herokuapp.com/species/")
species_list = species_data.json()
species = []

for i in range(0,len(species_list)):
    film_url = species_list[i]["films"]
    filmID = get_filmID(film_url)
    
    species1 = Species(species_list[i]["id"],species_list[i]["classification"],species_list[i]["eye_colors"],species_list[i]["hair_colors"],filmID)
    species.append(species1)


#grabbing people data
people_data = requests.get("https://ghibliapi.herokuapp.com/people/")
people_list = people_data.json()
people=[]

for i in range(0,len(people_list)):

    film_url = people_list[i]["films"]
    filmID = get_filmID(film_url)

    if  people_list[i]["id"] not in ["2409052a-9029-4e8d-bfaf-70fd82c8e48d","2a1dad70-802a-459d-8cc2-4ebd8821248b"] :
        species_url = people_list[i]["species"]
        species_data = requests.get(species_url)
        species_list = species_data.json()
        speciesID = species_list["id"]
        
        person = People(people_list[i]["name"],people_list[i]["gender"],people_list[i]["eye_color"],people_list[i]["hair_color"],filmID,speciesID)
        people.append(person)

#grabbing location data
location_data = requests.get("https://ghibliapi.herokuapp.com/locations/")
location_list = location_data.json()
locations = []

for i in range(0,len(location_list)):
    film_url = location_list[i]["films"]
    filmID = get_filmID(film_url)
    
    location = Location(location_list[i]["name"],location_list[i]["climate"],location_list[i]["terrain"],filmID)

    locations.append(location)

#grabbing vehicle data
vehicle_data = requests.get("https://ghibliapi.herokuapp.com/vehicles/")
vehicle_list = vehicle_data.json()
vehicles = []

for i in range(0,len(vehicle_list)):
    film_url = vehicle_list[i]["films"]
    filmID = get_filmID(film_url)
    
    vehicle = Vehicle(vehicle_list[i]["name"],vehicle_list[i]["vehicle_class"],vehicle_list[i]["length"],filmID)
    vehicles.append(vehicle)

#some sample query
print(films[5])
print(species[3])
print(people[2])
print(locations[1])
print(vehicles[0])

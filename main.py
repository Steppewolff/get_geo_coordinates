from os.path import exists

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# Lista de hospitales
hospitales = [
    "C.H. Ciudad de Jaén", "Corporació Sanitària Parc Taulí", "Hospital 12 Octubre",
    "Hospital A Coruña", "Hospital Álava", "Hospital Bellvitge", "Hospital Cabueñes",
    "Hospital Clínico Lozano Blesa", "Hospital Clinic", "Hospital de Burgos",
    "Hospital de Castellón", "Hospital de Guadalajara", "Hospital de Jerez",
    "Hospital de La Fé", "Hospital de Pontevedra", "Hospital de Salamanca",
    "Hospital de Jerez", "Hospital Doctor Negrín", "Hospital General de Valencia",
    "Hospital Germans Trias i Pujol", "Hospital Getafe", "Hospital La Princesa",
    "Hospital Manacor", "Hospital Marqués de Valdecilla", "Hospital Miguel Servet",
    "Hospital Mutua de Terrasa", "Hospital Puerta del Mar", "Hospital Ramón y Cajal",
    "Hospital Reina Sofía", "Hospital Royo Villanova", "Hospital Santa Creu i Sant Pau",
    "Hospital Santiago de Compostela", "Hospital Son Llàtzer", "Hospital Vall d´Hebron",
    "Hospital Virgen Arrixaca", "Hospital Virgen de la Macarena",
    "Hospital Virgen de la Victoria", "Hospital Virgen del Rocío", "Hospital Can Misses",
    "Hospital Son Espases", "Hospital del Mar", "Hospital Verge de la Cinta",
    "Hospital Santos Reyes", "Hospital de Ciudad Real", "Hospital de Badajoz",
    "Hospital Arquitecto Marcide", "Hospital Lucus Augusti", "Hospital de Ourense",
    "Hospital San Pedro", "Hospital Gregorio Marañón", "Hospital Puerta de Hierro",
    "Clínica de Navarra"
]

geolocator = Nominatim(user_agent="hospital_locator")

# Diccionario para guardar las coordenadas
coordenadas = {}

# Obtener las coordenadas para cada hospital
for hospital in hospitales:
    location = geolocator.geocode(hospital, timeout=10)
    if location:
        coordenadas[hospital] = (round(location.latitude, 4), round(location.longitude, 4))
        print(f"{hospital}: {coordenadas[hospital]}")
    else:
        print(f"No se encontraron coordenadas para {hospital}")
    time.sleep(1)  # Respetar los límites de la API

# Imprimir todas las coordenadas
print(coordenadas)

# Escribir coordenadas a un archivo
if exists("./output/coordenadas.txt"):
    with open("./output/coordenadas.txt", "a") as file:
        for hospital, coordenada in coordenadas.items():
            file.write(f"{hospital}: {coordenada}\n")
else:
    with open("./output/coordenadas.txt", "w") as file:
        for hospital, coordenada in coordenadas.items():
            file.write(f"{hospital}: {coordenada}\n")

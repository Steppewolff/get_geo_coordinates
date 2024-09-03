from fileinput import close

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

file_sql = open("./output/coord_sql_script.sql", "w")

with open("./output/coordenadas.txt", "r") as file:
    for line in file:
        hospital, coordenada = line.split(": ")
        coordenada = coordenada.strip()
        coordenada = coordenada[1:-1]
        lat, lon = coordenada.split(", ")
        file_sql.write(f"UPDATE hospital SET geo_latitude = {lat}, geo_longitude = {lon} WHERE hospital_name = '{hospital}';\n")

close("./output/coord_sql_script.sql")

close("./output/coordenadas.txt")
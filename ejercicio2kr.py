import json
import re

# Función para extraer datos y aca basicamente use eso para las expresiones regulares, si no entiendes me avisas
def extract_from_regex(regex, contenido): 
    return re.findall(regex, contenido) if contenido else []

# Expresión regular corregida
regex = (
    r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\["  
    r"(\d{2}/[a-zA-Z]{3}/\d{4}):"  
    r"(\d{2}:\d{2}:\d{2})\s\+\d{4}"  
    r"\]\s\"([A-Z]+)" #Esta parte supongo que la entiendes, capturar la IP, la fecha, la hora,etc.
)

# Abrir y leer el archivo y pues de una vez hacerlo de manera segura
ruta_archivo = r"C:\\Users\\carol\\Downloads\\log\\access.log" #En este caso yo movi el archivo al escritorio y creando una carpeta y asi moviendo el archivo, el problema que vi es que no leia
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()


resultado = extract_from_regex(regex, contenido)

# Imprimes los resultados
for ip, fecha, hora, metodo in resultado:
    print(f"La IP es: {ip}, la fecha es: {fecha}, la hora es: {hora}, el método es: {metodo}")
import re

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        contenido = file.read()
    # Ejemplo: Buscar patrones como "192.168.1.1 2023-10-05 14:30 GET"
    regex = r'(\d+\.\d+\.\d+\.\d+)\s+(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2})\s+(\w+)'
    resultado = re.findall(regex, contenido)
    return resultado

if _name_ == "_main_":
    resultado = leer_archivo("log.txt")  # Reemplaza "archivo.txt" con tu archivo
    for i in range(len(resultado)):
        print(f"La ip es: {resultado[i][0]}, la fecha es: {resultado[i][1]}, la hora es: {resultado[i][2]} y el método es: {resultado[i][3]}")
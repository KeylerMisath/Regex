import re
import json

# Listas para almacenar los valores únicos
ipsAlmacenadas = set()
fechasAlmacenadas = set()
metodosAlmacenados = set()
codigos_errorAlmacenados = set()

# Función para extraer con expresiones regulares
def extractFromRegularExpression(regex, data):
    if data:
        return re.findall(regex, data)
    return None

# Expresión regular 
regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s\-\s\-\s\[(\d{2}\/[a-zA-Z]{3}\/\d{4}):(\d{2}:\d{2}:\d{2})\s\+\d{4,10}\]\s\"([A-Z]{3,7})\s(\/\S+)\s+HTTP\/\d{1}\.\d{0,1}\"\s(\d{3})"

# Leer el archivo de logs
with open("C:\\Users\\carol\\Downloads\\log\\access.log", "r") as file:
    data = file.read()

# Extraer los datos
resultado = extractFromRegularExpression(regex, data)

# Recorrer resultados y almacenar valores únicos
if resultado:
    for ip, fecha, hora, metodo, _, codigo in resultado:
        ipsAlmacenadas.add(ip)
        fechasAlmacenadas.add(fecha)
        metodosAlmacenados.add(metodo)
        codigos_errorAlmacenados.add(codigo)

# Convertir a listas
datos_extraidos = {
    "IPs Unicas": list(ipsAlmacenadas),
    "Fechas Unicas": list(fechasAlmacenadas),
    "Metodos HTTP": list(metodosAlmacenados),
    "Codigos de Error": list(codigos_errorAlmacenados)
}

# Imprimir resultados únicos
print(json.dumps(datos_extraidos, indent=4))

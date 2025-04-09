import json, re, requests

ipsAlmacenadas = set()
fechasAlmacenadas = set()
metodosAlmacenados = set()
codigos_errorAlmacenados = set()

def extractFromRegularExpression(regex, data):
    if data:
        return re.findall(regex, data)
    return None

regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\[(\d{2}\/[a-zA-Z]{3}\/\d{4})(\:\d{2}\:\d{2}\:\d{2}).*?(\"\b[A-Z]{1,7}\s\S+\s\S+)\s(\d{3})"

# Leer y combinar todos los logs
data = ""
for i in range(7):
    ruta = fr"C:\Users\carol\Downloads\SotM34-anton\SotM34\http\access_log{'' if i == 0 else '.' + str(i)}"
    with open(ruta, "r") as file:
        data += file.read()

# Extraer datos
resultado = extractFromRegularExpression(regex, data)

# Guardar IPs únicas y otros datos
if resultado:
    for ip, fecha, hora, url, codigo in resultado:
        ipsAlmacenadas.add(ip)
        fechasAlmacenadas.add(fecha)
        codigos_errorAlmacenados.add(codigo)

# Llamar a la API por cada IP única
datosGeolocalizados = []
for ip in ipsAlmacenadas:
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        geoInfo = {
            "ip": ip,
            "pais": response.get("country"),
            "ciudad": response.get("city"),
            "codigo": response.get("code")
        }
    except Exception as e:
        geoInfo = {
            "ip": ip,
            "pais": None,
            "ciudad": None,
            "codigo": None
        }
    datosGeolocalizados.append(geoInfo)

# Mostrar en consola en formato bonito
print(json.dumps(datosGeolocalizados, indent=4, ensure_ascii=False))

# (Opcional) Guardar resultado en archivo
with open("ips_geolocalizadas.json", "w", encoding="utf-8") as f:
    json.dump(datosGeolocalizados, f, indent=4, ensure_ascii=False)

import re
from collections import Counter

# Expresión regular para extraer el navegador
user_agent_regex = re.compile(r'"[^"]*"$')

# Expresión para detectar el navegador dentro del User-Agent
browser_regex = re.compile(r'(MSIE|Trident|Edg|Edge|Chrome|Firefox|OPR|Opera|Safari)(?=/)')

# Diccionario para contar navegadores
browser_counts = Counter()

# Leer el archivo de logs
with open("access.log", "r", encoding="utf-8") as log_file:
    for line in log_file:
        user_agent_match = user_agent_regex.search(line)
        if user_agent_match:
            user_agent = user_agent_match.group(0)
            browser_match = browser_regex.search(user_agent)
            if browser_match:
                browser = browser_match.group(1)
                # Unificar OPR y Opera, Edg y Edge
                if browser == "OPR":
                    browser = "Opera"
                elif browser == "Edg":
                    browser = "Edge"
                browser_counts[browser] += 1
            else:
                browser_counts["Otros navegadores"] += 1

# Mostrar resultados
print("Navegadores detectados:")
for browser, count in browser_counts.items():
    print(f"{browser}: {count}")

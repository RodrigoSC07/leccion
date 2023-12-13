import locale
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
driver = webdriver.Chrome()
url = "https://datosmacro.expansion.com/pib/ecuador"
driver.get(url)
contenido = driver.page_source
soup = BeautifulSoup(contenido, 'html.parser')
tabla_pib = soup.find('table')
filas = tabla_pib.find_all('tr')

fechas = []
pib = []
var = []

for fila in filas[1:]:
    columnas = fila.find_all('td')
    fechas.append(columnas[0].text.strip())
    pib_valor = columnas[2].text.strip().replace('M$', '').replace('.', '')
    pib.append(pib_valor)
    var.append(columnas[3].text.strip())

print("Fechas:")
for fecha in fechas:
    print(fecha)

print("\nPIB Anual:")
for pib in pib:
    print(pib)

print("\nVariacion del PIB %:")
for var_pib in var:
    print(var_pib)

df = pd.DataFrame({'Fecha': fechas, 'PIB Anual': pib, 'Var.PIB %': var})
df.to_csv('Date.csv', index=False)

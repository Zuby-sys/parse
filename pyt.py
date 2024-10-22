import requests
import csv
from bs4 import BeautifulSoup

url = 'https://vecher-s-soloviev.com/'

fulltitles = []
fulldescript = []

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all(class_='sres-text')
    description = soup.find_all(class_='sres-desc')
    if titles:
        for title in titles:
            link_text = title.get_text(strip=True)
            fulltitles.append(link_text)
    if description:
        for desc in description:
            link_text = desc.get_text(strip=True)
            fulldescript.append(link_text)

for i in range(len(fulltitles)):
    print(str(i+1)+" Cтатья. Название:\n"+fulltitles[i])
    print("Описание:")
    print(fulldescript[i])
    print("\n")

filename = 'hzhz.csv'

with open(filename, mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(['Название', 'Описание'])
    
    for item in range(len(fulltitles)):
        writer.writerow([fulltitles[item], fulldescript[item]])





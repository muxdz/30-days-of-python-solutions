import requests
import json
import re
from bs4 import BeautifulSoup

url = 'https://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

data = {
    "title": soup.title.get_text(strip=True),
    "facts": []
}

for heading in soup.find_all('h3'):
    name = heading.get_text(" ", strip=True)

    parent_text = heading.parent.get_text(" ", strip=True)

    value = parent_text.replace(name, "", 1).strip()

    if value:
        data["facts"].append({
            "name": name,
            "value": value
        })

with open('day22/boston_uni.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

    
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", class_="wikitable")

rows = table.find_all("tr")

presidents = []

for row in rows[:5]:
    print(row.get_text(" ", strip=True))

presidents = []

for row in rows[1:]:  # skip table header
    cells = row.find_all(["th", "td"])

    values = []

    for cell in cells:
        values.append(cell.get_text(" ", strip=True))

    if values:
        presidents.append(values)

with open("day22/presidents.json", "w", encoding="utf-8") as file:
    json.dump(presidents, file, indent=4, ensure_ascii=False)
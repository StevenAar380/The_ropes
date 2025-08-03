import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.classcharts.com/mobile/student#5529766,announcements")
soup = BeautifulSoup(response.text, "html.parser")

print(soup)


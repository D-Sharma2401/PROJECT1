#WEB SCRAPPING:)
#pip install beautifulsoup4
#pip install requests
import requests
from bs4 import BeautifulSoup

url = "https://www.indiatoday.in/sports"
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup, type(soup), id(soup))
# print(soup.prettify())

#tags = soup.find_all("h3")
tags = soup.find_all("div",class_="https://www.indiatoday.in/sports")
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,")

print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,")
from bs4 import *
import requests

r = requests.get('https://www.python.org/').text
soup = BeautifulSoup(r)

links = []

for row in soup.find_all('a', href=re.compile('/events/python-events/\d+')):
    links.append((row.text))

print(links)

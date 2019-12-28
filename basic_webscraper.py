import requests
from bs4 import BeautifulSoup

page = requests.get("https://offsecnewbie.com")
soup = BeautifulSoup(page.content)

for title in soup.find_all(class_="post-title"):
    print(title.get_text())
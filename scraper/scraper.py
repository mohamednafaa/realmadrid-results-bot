import requests
from bs4 import BeautifulSoup

url_champions_league = "https://www.liveonsat.com/club-uefa-champions-league.php"
url_spain = "https://www.liveonsat.com/europe-spain-all-football.php"

response_cl = requests.get(url_champions_league)
response_spain = requests.get(url_spain)

content_cl = BeautifulSoup(response_cl.content, "html.parser")
content_spain = BeautifulSoup(response_spain.content, "html.parser")


# Get Real Madrid matches in Champions League
matches_cl = content_cl.find_all(class_="fLeft")

for m in matches_cl:
    teams = m.get_text()
    if "Real Madrid" in teams:
        print("Real Madrid Champions League Match Found:", teams)

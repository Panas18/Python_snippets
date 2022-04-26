from bs4 import BeautifulSoup
import requests

url = "https://kathmandupost.com/"
source = requests.get(url).text

soup = BeautifulSoup(source, "lxml")

for article in soup.find_all("article"):
    headline = article.find("h3")
    if headline is not None:
        print(headline.text)
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

for img in soup.find_all("img"):
    print(img)

print(soup.title.string)

print(soup.find_all("img", src="/static/grapes.png"))
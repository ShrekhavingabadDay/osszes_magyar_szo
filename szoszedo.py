import requests
from bs4 import BeautifulSoup

szavak = []

betuk = ['a', 'b', 'c', 'cs', 'd', 'dz', 'dzs', 'e', 'é', 'f', 'g', 'gy', 'h', 'i', 'j', 'k', 'l', 'ly', 'm', 'n', 'ny', 'o', 'ö', 'ő', 'p', 'q', 'r', 's', 'sz', 't', 'ty', 'u', 'ú', 'ü', 'v', 'w', 'x', 'y', 'z', 'zs']

for betu in betuk:
    r = requests.get("https://hu.wiktionary.org/wiki/Index:Magyar/"+betu)

    soup = BeautifulSoup(r.text, 'html.parser')

    osszes_p = soup.find_all('p')[1:-2]

    for p in osszes_p:
        szavak += p.text.strip().split('\n')
with open('osszes_magyar_szo.txt', 'w') as fajl:
    fajl.write('\n'.join(szavak))

import requests, os, bs4
print(os.getcwd())
url = 'https://xkcd.com/2700'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Pobieranie strony %s' % url)
    res =requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,features="html.parser")
    comicElem = soup.select('#comic img')                       # wszystkie elementy o nazwie img które zostały umieszczone
    if comicElem ==[]:                                          # w elemencie którego atrybut id ma wartość comic
        print('Nie udało się odnaleźć pliku obrazu komiksu')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')            # pobieramy wartość atrubutu src
        print('Pobieranie obrazu %s...' %(comicUrl))            # dodajemy wczesniej http bo src ma postać = //imgs.xkcd.com/comics/attention_span.png
        res = requests.get(comicUrl)                            # Przekazujemy funkcji get adres obrazka
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') # otwieramy plik do zapisu obrazu
        for chunk in res.iter_content(100000):                                   # dzielimy na paczki
            imageFile.write(chunk)                                               # Zapisujemy w pliku
        imageFile.close()
    nextLink = soup.select('a[rel="next"]')[0]                                   # selektor znajduje wszystkie elementy o nazwie a które maja
    url = 'http://xkcd.com'+nextLink.get('href')                                 # atrybut o nazwie rel o wartości "next"

print('Gotowe')

from urllib.request import urlopen

url = 'https://mucollabo.github.io/movie_app_2020/'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)
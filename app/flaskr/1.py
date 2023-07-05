import requests, json
geo_url=requests.get(
geoapi=json.loads(geo_url)
for i in geoapi['result']:
    print(i['addressMatches'])
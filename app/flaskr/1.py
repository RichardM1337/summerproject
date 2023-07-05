import requests, json
geo_url=requests.get("https://geocoding.geo.census.gov/geocoder/geographies/address?street=4600+Silver+Hill+Rd&city=Washington&state=DC&benchmark=Public_AR_Census2020&vintage=Census2020_Census2020&layers=10&format=json").text
geoapi=json.loads(geo_url)
for i in geoapi['result']:
    print(i['addressMatches'])
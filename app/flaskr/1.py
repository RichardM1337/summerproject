import requests, json
zip=10312
geo_url=requests.get(f"http://api.weatherapi.com/v1/current.json?key=581f26cd97c24faa809164418230507&q={zip}&aqi=no").text
geoapi=json.loads(geo_url)
print(geoapi['current'])
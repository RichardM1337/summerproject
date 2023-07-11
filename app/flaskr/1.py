import requests, json
from flask import request
geo_url=requests.get(f"https://api.weatherapi.com/v1/current.json?key=581f26cd97c24faa809164418230507&q=00000&aqi=yes").text
geoapi=json.loads(geo_url)
zipcode = request.form.get('zipcode')
print(zipcode)


   # {% endfor %}
   # {% for i in geoapi['location'] %}
   #     <h2>{{i['name']}} , {{i['region']}} , {{i['country']}} </h2>
   # {% endfor %}

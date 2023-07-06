import requests, json
geo_url=requests.get(f"https://api.weatherapi.com/v1/current.json?key=581f26cd97c24faa809164418230507&q=150315&aqi=no").text
geoapi=json.loads(geo_url)
print(geoapi["current"])
print(geoapi['current']['temp_f'])



   # {% endfor %}
   # {% for i in geoapi['location'] %}
   #     <h2>{{i['name']}} , {{i['region']}} , {{i['country']}} </h2>
   # {% endfor %}

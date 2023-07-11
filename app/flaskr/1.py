import requests, json
zipcode=int( input("what ius ur zicpode : lol!!!"))
geo_url=requests.get(f"https://api.weatherapi.com/v1/current.json?key=581f26cd97c24faa809164418230507&q={zipcode}&aqi=yes").text
geoapi=json.loads(geo_url)
print(geoapi)

   # {% endfor %}
   # {% for i in geoapi['location'] %}
   #     <h2>{{i['name']}} , {{i['region']}} , {{i['country']}} </h2>
   # {% endfor %}

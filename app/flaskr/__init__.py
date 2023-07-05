import os

from flask import Flask, render_template, json, request
import requests
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/")
    def home():
        return render_template('home.html')
    def weather():
        street = request.form.getlist('street')
        city = request.form.getlist('city')
        ini = request.form.getlist('ini')
        zipcode = request.form.getlist('zip')
        geo_url=requests.get("https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={street}{city}{ini}{zipcode}&benchmark=Public_AR_Census2020&vintage=Census2020_Census2020&layers=10&format=json")
        geoapi=json.loads(geo_url)
        for i in geoapi["Census Blocks"]:
        weather_url=requests.get("")
    return app
    
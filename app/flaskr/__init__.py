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
    @app.route("/weather/<zipcode>", methods=['GET','POST'])
    def weather(zipcode):
        zipcode = request.form['zipcode']
        geo_url=requests.get(f"http://api.weatherapi.com/v1/current.json?key=581f26cd97c24faa809164418230507&q={zipcode}&aqi=yes").text
        geoapi=json.loads(geo_url)
        return render_template('weather.html',geoapi=geoapi,zipcode=zipcode)
    @app.errorhandler(404)
    def error(e):
        return render_template('error.html')
    return app

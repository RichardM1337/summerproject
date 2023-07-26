from flask import Flask, render_template, json, request, redirect
import os, sys, requests

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

    @app.route("/")
    def home():
        return render_template('home.html')
        
        
    @app.route("/weather/<identifier>", methods=['GET','POST'])
    def weather(identifier):
        identifier = request.args.get('identifier')
        geo_url=requests.get(f"http://api.weatherapi.com/v1/current.json?key=581f26cd97c24faa809164418230507&q={identifier}&aqi=yes").text
        geoapi=json.loads(geo_url)
        if "error" in geoapi:
            return render_template('404.html', geoapi=geoapi)
        else:
            return render_template('weather.html',geoapi=geoapi)

    """@app.route("/weather2", methods=['GET','POST'])
    def weather2():
        try:
            zipcode = request.form.get('zipcode')
            geo_url=requests.get(f"http://api.weatherapi.com/v1/current.json?key=581f26cd97c24faa809164418230507&q={zipcode}&aqi=yes").text
            geoapi=json.loads(geo_url)
            return render_template('weather2.html',geoapi=geoapi,zipcode=zipcode)
        
        except:
            return redirect("/404")

    @app.route("/test")
    def test():
        try:
            return render_template("test.html")
        
        except:
            return redirect("/404")"""

    @app.errorhandler(404)
    def error(e):
        return render_template('404.html')

    return app

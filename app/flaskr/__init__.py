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

    # a simple page that says hello
    @app.route("/")
    def home():
        try:
            return render_template('home.html')
        
        except:
            return redirect("/404")
        
    @app.route("/weather", methods=['GET','POST'])
    def weather():
        try:
            zipcode = request.form.get('zipcode')
            geo_url=requests.get(f"http://api.weatherapi.com/v1/current.json?key=581f26cd97c24faa809164418230507&q={zipcode}&aqi=yes").text
            geoapi=json.loads(geo_url)
            return render_template('weather.html',geoapi=geoapi,zipcode=zipcode)
        
        except:
            return redirect("/404")

    @app.route("/404")
    def error():
        try:
            render_template("404.html")
        
        except:
            return redirect("/404")

    return app
    
#        return render_template('index.html')
#    
#    @app.route("/404")
#    def error():
#        return render_template('404.html')

#    @app.route("weather/<path:zip>")
#    
#    return app

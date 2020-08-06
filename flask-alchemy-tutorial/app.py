from flask import Flask, request, redirect, url_for, render_template
import requests, json
from flask_sqlalchemy import SQLAlchemy
from opencage.geocoder import OpenCageGeocode
from pprint import pprint

app = Flask(__name__)

opencage_key 
openweather_key

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        address = request.form['content']
        try:
            return redirect('/')
        except:
            return "um bug with form"
        # return render_template("base.html")
        # print(address)
    else:
        return render_template("base.html")

def CashmereOrCotton(openweather_key, opencage_key, address):

    geocoder = OpenCageGeocode(opencage_key)

    address = u'Los Angeles'

    results = geocoder.geocode(address)
    lat = results[0]['geometry']['lat']
    lang = results[0]['geometry']['lng']

    url = 'https://api.openweathermap.org/data/2.5/weather?lat='+str(lat)+'&lon='+str(lang)+'&appid='+openweather_key+'&units='+'metric'
    r = requests.get(url).json()

    a_temp = r['main']['temp']
    a_description = r['weather'][0]['description']
    # print(r['main']['temp'])
    # print(r['weather'][0]['description'])

    if a_temp <= 18:
        wear = "cashmere"
    else:
        wear = "cotton"

    return wear

if __name__ == "__main__":
    app.run(debug=True)

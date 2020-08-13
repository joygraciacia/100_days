import requests, json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from opencage.geocoder import OpenCageGeocode
from pprint import pprint

opencage_key = '22798f5e7e1e475c94fe1efd3f9b865f'
openweather_key = '94a75533eb9b0d50f5599add4552265d&'

geocoder = OpenCageGeocode(opencage_key)

@app.route('/'):
    return render_template('weather.html')

#stuff stuff
address = u'Los Angeles'
# glendon = u'1041 Glendon Ave, Los Angeles, CA, USA'
results = geocoder.geocode(address)
lat = results[0]['geometry']['lat']
lang = results[0]['geometry']['lng']
# pprint(lat)
# pprint(lang)

url = 'https://api.openweathermap.org/data/2.5/weather?lat='+str(lat)+'&lon='+str(lang)+'&appid='+openweather_key+'&units='+'metric'
r = requests.get(url).json()

a_temp = r['main']['temp']
a_description = r['weather'][0]['description']
print(r['main']['temp'])
print(r['weather'][0]['description'])

if a_temp <= 18:
    print("Wear cashmere")
else:
    print("Wear cotton")

if __name__ == '__main__':
    app.run()

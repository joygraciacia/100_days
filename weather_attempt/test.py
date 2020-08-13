from flask import Flask, render_template, request
import requests
# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request


app = Flask(__name__)

@app.route('/')
def weather():
       # your API key will come here
    # source contain json data from api
    # source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q =' + city + '&appid =' + api).read()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=94a75533eb9b0d50f5599add4552265d&'
    city = 'Las Vegas'

    r = requests.get(url.format(city)).json()
    print(r)

    return render_template('sample.html')



if __name__ == '__main__':
    app.run(debug = True)

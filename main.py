#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from weather import model
from collections import defaultdict

Dict = defaultdict(list)

app = Flask(__name__)
# you can set key as config
app.config['GOOGLEMAPS_KEY'] = " AIzaSyAkbnmUc1VrprMq1PFMPCdlbPa6zWc_1gE "

# Initialize the extension
GoogleMaps(app)
@app.route('/')
def index():
    return render_template('quakesim.html')

@app.route('/about', methods = ['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/start', methods = ['GET', 'POST'])
def start():
    return render_template(
        'weather.html',
        cities = [{'name': 'None'},
        {'name': 'Mumbai'},
        {'name': 'Chennai'},
        {'name': 'Delhi'},
        {'name': 'Pune'}, 
        {'name': 'Kochi'}, 
        {'name': 'Patna'}, 
        {'name': 'Varanasi'},
        {'name': 'Kanpur'},
        {'name': 'Agra'},
        {'name': 'Ahmedabad'},
        {'name': 'Kolkata'},
        {'name': 'Srinagar'},
        {'name': 'Bangalore'},
        {'name': 'Nagpur'},
        {'name': 'Indore'},
        {'name': 'Trivandrum'},
        {'name': 'Panjim'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    city_probability = {'None': 1,
    'Mumbai': 7,
    'Chennai': 4,
    'Delhi': 12,
    'Pune': 4,
    'Kochi': 4,
    'Patna': 14,
    'Varanasi': 9,
    'Kanpur': 10,
    'Agra': 9,
    'Ahmedabad': 12,
    'Kolkata': 9,
    'Srinagar': 47,
    'Bangalore': 4,
    'Nagpur': 5,
    'Indore': 7,
    'Trivandrum': 3,
    'Panjim': 3
    }
    error = None
    city = request.form.get('comp_city')
    select1 = request.form.get('comp_select1')
    select2 = request.form.get('comp_select2')
    select3 = request.form.get('comp_select3')
    select4 = request.form.get('comp_select4')
    select5 = request.form.get('comp_select5')
    select6 = request.form.get('comp_select6')
    select7 = request.form.get('comp_select7')
    select8 = request.form.get('comp_select8')
    resp = model(select1, select2, select3, select4, select5, select6, select7, select8)
    risk = int(resp)*int(city_probability[city])
    return render_template(
        'result.html',
        data=resp,
        risk=risk,
        city=city,
        error=error)

@app.route("/map", methods=['GET', 'POST'])
def mapview():
    mymap = Map(
        identifier="view-side",
        style="height:540px;width:1270px;margin:0;",
        lat=19.07283,
        lng=78.88261,
        markers=[(19.07283,72.88261)],
        fullscreen_control=True,
        zoom=6
    )
    return render_template(
        'map.html', 
        mymap=mymap, 
        cities = [{'name': 'None'},
        {'name': 'Mumbai'},
        {'name': 'Chennai'},
        {'name': 'Delhi'},
        {'name': 'Pune'}, 
        {'name': 'Kochi'}, 
        {'name': 'Patna'}, 
        {'name': 'Varanasi'},
        {'name': 'Kanpur'},
        {'name': 'Agra'},
        {'name': 'Ahmedabad'},
        {'name': 'Kolkata'},
        {'name': 'Srinagar'},
        {'name': 'Bangalore'},
        {'name': 'Nagpur'},
        {'name': 'Indore'},
        {'name': 'Trivandrum'},
        {'name': 'Panjim'}])

@app.route("/city", methods=['GET', 'POST'])
def city():
    city_probability = {'None': 1,
    'Mumbai': 7,
    'Chennai': 4,
    'Delhi': 12,
    'Pune': 4,
    'Kochi': 4,
    'Patna': 14,
    'Varanasi': 9,
    'Kanpur': 10,
    'Agra': 9,
    'Ahmedabad': 12,
    'Kolkata': 9,
    'Srinagar': 47,
    'Bangalore': 4,
    'Nagpur': 5,
    'Indore': 7,
    'Trivandrum': 3,
    'Panjim': 3
    }
    city = request.form.get('city_select')
    Dict['city'] = city
    Dict['probability'] = city_probability['city']

    return render_template('city.html', 
        city=city, 
        probability=city_probability[city],
        Height_ft=[{'name':1},{'name':2}],
        condition=[{'name':1},{'name':2}],
        floor_count=[{'name':1},{'name':2}],
        ward_id=[{'name':1},{'name':2}],
        area_sqft=[{'name':1},{'name':2}])

@app.route("/city_result")
def city_result():
    select1 = request.form.get('comp_select1A')
    select2 = request.form.get('comp_select2A')
    select3 = request.form.get('comp_select3A')
    select4 = request.form.get('comp_select4A')
    select5 = request.form.get('comp_select5A')
    data = model(select1, select2, select3, select4, select5)
    city = Dict['city']
    risk = Dict['probability']*data
    render_template('city_result.html', city=city, risk=risk, data=data)

if __name__=='__main__':
    app.run(debug=True)

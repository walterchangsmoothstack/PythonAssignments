from flask import Flask, json, render_template, request, jsonify
from utopia import app
from utopia.models import Airport
from utopia.Service.Airline import Airline
import logging


@app.route('/airlines/add/airport', methods=['POST'])
def addAirport():

    airline_service = Airline()
    return airline_service.createAirport(request.json)


@app.route('/airlines/read/airport')
def readAllAirports():

    airline_service = Airline()
    airports = airline_service.readAirport()
    return airports

@app.route('/airlines/add/route', methods=['POST'])
def addRoute():

    airline_service = Airline()
    return airline_service.addRoute(request.json)

@app.route('/airlines/read/route', methods=['GET'])
def readAllRoutes():

    airline_service = Airline()
    routes = airline_service.readRoute()
    
    return routes



    # cur = db.connection.cursor()
    # result_value = cur.execute('SELECT * FROM airport')
    

    # columns = [x[0] for x in cur.description]
    # data = cur.fetchall()
    # json_data = []
    # for result in data:
    #     json_data.append(dict(zip(columns, result)))

    # logging.info("Select all airports from utopia.airports", json_data)
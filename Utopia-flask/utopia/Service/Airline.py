from flask import Flask, app, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields

from utopia.models.Airport import Airport, Route
from utopia import Session

import logging, json, traceback

logging.basicConfig(level=logging.INFO)

ma = Marshmallow(app)



class RouteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Route
    id = auto_field()
    origin_id = auto_field()
    destination_id = auto_field()

class AirportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Airport
    iata_id = auto_field()
    city = auto_field()
    incoming = fields.List(fields.Nested(RouteSchema))
    outgoing= fields.List(fields.Nested(RouteSchema))



class Airline:

    def __init__(self):
	    self = self

    def createAirport(self, airport):

        logging.info("Create Airport")
        logging.info(airport)
        
        new_airport = Airport(iata_id= airport['iata_id'], city = airport['city'])
        try:
            session = Session()
            
            session.add(new_airport)

            logging.info("Adding routes to the database if any are listed")

            for route in airport['incoming']:
               session.add(Route(origin_id=route['origin_id'], destination_id=route['destination_id']))

            for route in airport['outgoing']:
                session.add(Route(origin_id=route['origin_id'], destination_id=route['destination_id']))

            session.commit()
        except:
            logging.error("Error saving into engine")
            traceback.print_exc()
            session.rollback()
        else:
            return airport
        finally:
            session.close()
    
    def readAirport(self):

        logging.info("Reading all airports")
        
        json_data = []

        try:
            session = Session()
            airports = session.query(Airport).all()
            airport_schema = AirportSchema(many=True)

            return jsonify({'airports':airport_schema.dump(airports)})
        except:
            logging.error("Failed to retrieve airport table data")
            traceback.print_exc()
        finally:
            session.close()
    
    def addRoute(self, route):
        logging.info("Create Route")
        logging.info(route)
        new_route = Route(**route)
        try:
            session = Session()
            session.add(new_route)
            session.commit()
        except:
            logging.error("Error saving into engine")
            traceback.print_exc()
            session.rollback()
        else:
            return route
        finally:
            session.close()
    
    def readRoute(self):

        logging.info("Reading all routes")

        try:
            session = Session()

            routes = session.query(Route).all()
            route_schema = RouteSchema(many=True)
            return jsonify({"routes": route_schema.dump(routes)})
        except:
            logging.error("Failed to retrieve route table data")
            traceback.print_exc()
        finally:
            session.close()
        

        
    
    












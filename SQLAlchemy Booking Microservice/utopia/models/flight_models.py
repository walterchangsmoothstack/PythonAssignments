from flask import Flask
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import backref, relation, relationship
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields

from utopia import app, db
from sqlalchemy.dialects.mysql import FLOAT

# from utopia.models.models import Booking, Passenger, FlightBookings, BOOKING_SCHEMA, BOOKING_SCHEMA_MANY, PASSENGER_SCHEMA, PASSENGER_SCHEMA_MANY, FLIGHT_BOOKINGS_SCHEMA, FLIGHT_BOOKINGS_SCHEMA_MANY


ma = Marshmallow(app)


def generate_f_id():
    flight_ids = db.session.execute('SELECT id FROM flight')
    i=1
    for id in flight_ids:
        
        if i == id[0]:
            i+=1
        else:
            break
    return i

class Flight(db.Model):
    __tablename__ = 'flight'

    id = db.Column(db.Integer, primary_key=True, default=generate_f_id)
    route_id = db.Column(db.Integer, ForeignKey('route.id'))
    airplane_id = db.Column(db.Integer, ForeignKey('airplane.id'))
    departure_time = db.Column(db.DateTime)
    reserved_seats = db.Column(db.Integer)
    seat_price = db.Column(FLOAT(precision=None, scale=1))
    flight_bookings = relationship("FlightBookings", backref='flight')



class FlightSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Flight
        ordered = True
    id = auto_field()
    route_id = auto_field()
    airplane_id = auto_field()
    departure_time = auto_field()
    reserved_seats = auto_field()
    seat_price  = auto_field()
    # airplane = fields.Nested(AirplaneSchema(only=['id', 'airplane_type']))
    # route = fields.Nested(RouteSchema())
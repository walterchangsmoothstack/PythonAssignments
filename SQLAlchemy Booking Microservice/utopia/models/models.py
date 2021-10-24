from flask import Flask
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import backref, relation, relationship
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields
from utopia.models.flight_models import Flight
from utopia import app, db



ma = Marshmallow(app)


class FlightBookings(db.Model):
    __tablename__ = 'flight_bookings'

    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), primary_key=True)
    #flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'))


class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    is_active =  db.Column(db.Boolean, default=True)
    confirmation_code = db.Column(db.String(255))
    passengers = relationship('Passenger', backref='booking', lazy='subquery', cascade='all, delete')
    flight_bookings = relationship('FlightBookings', backref='booking', lazy='subquery', cascade='all, delete')

class Passenger(db.Model):
    __tablename__= 'passenger'

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'))
    given_name = db.Column(db.String(255))
    family_name = db.Column(db.String(255))
    dob = db.Column(db.String(10))
    gender = db.Column(db.String(45))
    address = db.Column(db.String(45))



class FlightBookingsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FlightBookings
    booking_id = auto_field()
    #flight_id = auto_field()

class PassengerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Passenger
        ordered = True
    id = auto_field()
    booking_id = auto_field()
    given_name = auto_field()
    family_name = auto_field()
    dob = auto_field()
    gender = auto_field()
    address = auto_field()

class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
        ordered = True
    id = auto_field()
    is_active = auto_field()
    confirmation_code = auto_field()

BOOKING_SCHEMA = BookingSchema()
PASSENGER_SCHEMA = PassengerSchema()
FLIGHT_BOOKINGS_SCHEMA = FlightBookingsSchema()

BOOKING_SCHEMA_MANY = BookingSchema(many=True)
PASSENGER_SCHEMA_MANY = PassengerSchema(many=True)
FLIGHT_BOOKINGS_SCHEMA_MANY = FlightBookingsSchema(many=True)
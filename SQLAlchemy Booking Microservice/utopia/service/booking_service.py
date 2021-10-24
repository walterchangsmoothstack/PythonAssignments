from flask import Flask, app, jsonify
from flask_sqlalchemy import SQLAlchemy
# from utopia.models.models import Booking, Passenger, FlightBookings, BOOKING_SCHEMA, BOOKING_SCHEMA_MANY, PASSENGER_SCHEMA, PASSENGER_SCHEMA_MANY, FLIGHT_BOOKINGS_SCHEMA, FLIGHT_BOOKINGS_SCHEMA_MANY
from utopia.models.flight_models import Booking, Passenger, FlightBookings, BOOKING_SCHEMA, BOOKING_SCHEMA_MANY, PASSENGER_SCHEMA, PASSENGER_SCHEMA_MANY, FLIGHT_BOOKINGS_SCHEMA, FLIGHT_BOOKINGS_SCHEMA_MANY
from utopia import db
from rstr import Rstr

import logging
logging.basicConfig(level=logging.INFO)


CONFIRMATION_CODE_LENGTH = 50

def generate_random_chars(length):
    rstr = Rstr()
    return rstr.xeger(r'[a-zA-Z0-9_.-]{'+str(length)+'}')


class BookingService:

##################### GET #####################

    def read_bookings(self):
        logging.info('reading all bookings')

        
        bookings = db.session.query(Booking).all()

        return jsonify({'bookings': BOOKING_SCHEMA_MANY.dump(bookings)})
    
    def find_booking(self, id):
        logging.info('finding booking with id %s ' %id)

        booking = Booking.query.get_or_404(id)

        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
        print(booking.flight_bookings)
        print(FLIGHT_BOOKINGS_SCHEMA.dump(booking.flight_bookings))

        return BOOKING_SCHEMA.dump(booking)

    def read_passengers(self):
        logging.info('reading all passengers')

        passengers = db.session.query(Passenger).all()

        return jsonify({'passengers' : PASSENGER_SCHEMA_MANY.dump(passengers)})

    def find_passenger(self, id):
        logging.info('finding passenger with id %s' %id)

        passenger = Passenger.query.get_or_404(id)

        return PASSENGER_SCHEMA.dump(passenger)



  ##################### POST #####################
  
    def add_booking_empty(self):
        logging.info('add an empty booking')

        booking = Booking(confirmation_code=generate_random_chars(CONFIRMATION_CODE_LENGTH))

        db.session.add(booking)
        db.session.commit()
        return BOOKING_SCHEMA.dump(booking)

    def add_passenger(self, passenger):
        logging.info('add passenger')

        passenger = Passenger(booking_id = passenger['booking_id'],
                    given_name = passenger['given_name'],
                    family_name=passenger['family_name'],
                    dob=passenger['dob'],
                    gender=passenger['gender'],
                    address=passenger['address']
        )
        db.session.add(passenger)
        db.session.commit()

        return PASSENGER_SCHEMA.dump(passenger)

    def add_passengers(self, passengers):
        logging.info('add passengers')

        passenger_list = []

        for passenger in passengers:
            passenger_to_add = Passenger(booking_id = passenger['booking_id'],
                        given_name = passenger['given_name'],
                        family_name=passenger['family_name'],
                        dob=passenger['dob'],
                        gender=passenger['gender'],
                        address=passenger['address']
            )
            passenger_list.append(passenger_to_add)

        db.session.bulk_save_objects(passenger_list, return_defaults=True)  
        db.session.commit()

        return jsonify({'passengers' : PASSENGER_SCHEMA_MANY.dump(passenger_list)})



##################### DELETE #####################


    def delete_booking(self, id):
        logging.info('delete booking with id %s' %id)

        booking = Booking.query.get_or_404(id)
        db.session.delete(booking)
        db.session.commit()

        return ''

    def delete_passenger(self, id):
        logging.info('delete passenger with id %s ' %id)

        passenger = Passenger.query.get_or_404(id)

        if len(passenger.booking.passengers) == 1:
            db.session.delete(passenger.booking)
        else:
            db.session.delete(passenger)
        db.session.commit()

        return ''
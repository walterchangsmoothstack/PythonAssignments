from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/utopia'
db = SQLAlchemy(app)
engine = create_engine('mysql://root:root@localhost/utopia', echo=True)
Session = sessionmaker(bind=engine)
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']

# mysql = MySQL(app)
from utopia import routes


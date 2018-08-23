from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sel import sel1
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Department(db.Model):
    div = db.Column(db.String(25), index=True, primary_key=True)
    gm = db.Column(db.String(50), index=True, nullable=False)
    drm = db.Column(db.String(50), index=True, unique=True, nullable=False) 
    clean = db.Column(db.String(50), index=True)
    staff= db.Column(db.String(30), index=True)
    irctc_staff = db.Column(db.String(30), index=True)
    irctc_care = db.Column(db.String(30), index=True)
    booking = db.Column(db.String(30), index=True)
    medical = db.Column(db.String(30), index=True)
    late = db.Column(db.String(30), index=True)
    water = db.Column(db.String(30), index=True)
    security = db.Column(db.String(30), index=True)
    electric = db.Column(db.String(30), index=True)
    none = db.Column(db.String(30), index=True)
    
class StationDivison(db.Model):
    station = db.Column(db.String(25), index=True, primary_key=True)
    div = db.Column(db.String(30), index=True)
		
		def __init__(self, divison, gm, drm):
			self.div = division
			self.gm = gm
			self.drm = drm
   
    def __repr__(self):
        return '<User {}>'.format(self.div) 
    
@app.route('/')
def rou():
    return sel1(request); 
    
if __name__ == '__main__':
    app.run(debug = True)
    
    

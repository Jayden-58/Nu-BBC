import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    second_name = db.Column(db.String(128), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    
class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    matrix_number = db.Column(db.String(128), nullable=True)
    artwork_url = db.Column(db.String(128), nullable=True)
    release_date = db.Column(db.Date, nullable=True)
    pressing_location =  db.Column(db.String(128), nullable=True)

class Publisher(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    date_founded = db.Column(db.Date, nullable=True)


class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    length = db.Column(db.Integer, nullable = True)


    



    


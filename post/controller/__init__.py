from flask import jsonify, render_template,request
from post import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
import re,uuid
import psycopg2,os




regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


def check(email):
    if(re.fullmatch(regex, email)):
        return True
    return False
from post.model.model import Person
def isPresent(unique_id1):
    cars = Person.query.all()
    for car in cars:
        if(str(car.unique_id)==str(unique_id1)):
            return True
    return False
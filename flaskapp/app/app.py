#!flask/bin/python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

class Couvert_Table(db.Model):
    __tablename__ = 'couvert_table'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    in_stock = db.Column('in_stock', db.Integer)
    price = db.Column('price', db.Integer)

    def __init__(self, id, title, in_stock, price):
        self.id = id
        self.title = title
        self.in_stock = in_stock
        self.price = price

class CouvertsList(Resource):
    def get(self):
        couverts = Couvert_Table.query.all()
        output = []
        for couvert in couverts:
            data = {}
            data['id'] = couvert.id
            data['title'] = couvert.title
            data['in_stock'] = couvert.in_stock
            data['price'] = couvert.price
            output.append(data)
        return jsonify({'couverts': output})

class Couvert(Resource):
    def get(self, id):
        couvert = Couvert_Table.query.filter_by(id=id).first()
        data = {}
        data['id'] = couvert.id
        data['title'] = couvert.title
        data['in_stock'] = couvert.in_stock
        data['price'] = couvert.price
        return jsonify({'couvert': data})

#routing
api.add_resource(CouvertsList, '/couverts')
api.add_resource(Couvert, '/couvert/<id>')

if __name__ == '__main__':
    app.run(debug=True)

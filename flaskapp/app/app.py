#!flask/bin/python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import reqparse, Resource, Api
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('couvert_id')
parser.add_argument('amount')

class Order_Table(db.Model):
    __tablename__= 'order_table'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    couvert_id = db.Column('couvert_id', db.String)
    amount = db.Column('amount', db.Integer)
    total_price = db.Column('total_price', db.Integer)

    def __init__(self, couvert_id, amount, total_price):
        self.couvert_id = couvert_id
        self.amount = amount
        self.total_price = total_price

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

class OrdersList(Resource):
    def get(self):
        orders = Order_Table.query.all()
        output = []
        for order in orders:
            data = {}
            data['id'] = order.id
            data['couvert_id'] = order.couvert_id
            data['amount'] = order.amount
            data['total_price'] = order.total_price
            output.append(data)
        return jsonify({'orders': output})

    def post(self):
        args = parser.parse_args()
        if args:
            try:
                couvert_id = args['couvert_id']
                amount = args['amount']
            except Exception:
                raise BadRequest('Please specify couvert_id and amount...')
            #get couvert to calculate price:
            couv= Couvert_Table.query.filter_by(id=couvert_id).first()
            data = {}
            data['couvert_id'] = couvert_id
            data['amount'] = amount
            data['total_price'] = int(amount) * int(couvert.price)
            order = Order_Table(data['couvert_id'], data['amount'], data['total_price'])
            db.session.add(order)
            db.session.commit()
            response = jsonify(data)
            response.status_code = 201
            return response
        raise BadRequest('Missing POST data') 

class Order(Resource):
    def get(self, id):
        order = Order_Table.query.filter_by(id=id).first()
        data = {}
        data['id'] = order.id
        data['couvert_id'] = order.couvert_id
        data['amount'] = order.amount
        data['total_price'] = order.total_price
        return jsonify({'order': data})

    def delete(self, id):
        try:
            order = Order_Table.query.filter_by(id=id).first()
        except Exception:
                raise BadRequest('Order does not exist..') 
        db.session.delete(order)
        db.session.commit()
        return True, 204 

#routing
api.add_resource(CouvertsList, '/couverts')
api.add_resource(Couvert, '/couvert/<id>')
api.add_resource(OrdersList, '/orders')
api.add_resource(Order, '/order/<id>')

if __name__ == '__main__':
    app.run(debug=True)

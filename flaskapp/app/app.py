#!flask/bin/python
from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from db import *


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('couvert_id')
parser.add_argument('count')


class CouvertsList(Resource):
    def get(self):
        return couverts

class OrderList(Resource):
    def get(self):
        return order

class Couvert(Resource):
    def get(self, id):
        return couverts[id]

    def delete(self, id):
       del couverts[id]
       return '', 204

class Order(Resource):
    def get(self):
        return order
    def post(self):
        args = parser.parse_args()
        print(order.keys)
        order_id = int(max(order.keys())) +1
        order[order_id] = {'couvert_id': args['couvert_id']}
        order[order_id].update({'count': args['count']})
        return order[order_id], 201

    def delete(self, article_id):
        del order[article_id]
        return '', 204

#routing couvert
api.add_resource(CouvertsList, '/couverts')
api.add_resource(Couvert, '/couvert/<id>')

#routing orders
api.add_resource(OrderList, '/orders')
api.add_resource(Order, '/order')

if __name__ == '__main__':
    app.run(debug=True)

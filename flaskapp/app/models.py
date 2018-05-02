# create database and add some data
from app import db
from app import Couvert_Table, Order_Table

# create database
db.create_all()

# data to add
couvert_01 = Couvert_Table(0, 'A4-Couvert', 20, 3)
couvert_02 = Couvert_Table(1, 'A3-Couvert', 20, 5)
couvert_03 = Couvert_Table(2, 'A2-Couvert', 20, 6)

test_order = Order_Table(1, 2, 10)

# commit to database
db.session.add(couvert_01)
db.session.add(couvert_02)
db.session.add(couvert_03)
db.session.add(test_order)
db.session.commit()

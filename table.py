from flask_sqlalchemy import SQLAlchemy
import csv

db = SQLAlchemy()


#  --- tạo bảng


class BOOK(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100))
    price = db.Column(db.Integer)
    number = db.Column(db.Integer)
    name = db.Column(db.String(100))
    address = db.Column(db.Text)
    phone = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, product, price, number, name, address, phone, email):
        self.product = product
        self.price = price
        self.number = number
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email


class FOOD(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True)
    msp = db.Column(db.String(100))
    name = db.Column(db.String(100))
    img = db.Column(db.Text)
    price = db.Column(db.Integer)

    def __init__(self, msp, name, img, price):
        self.msp = msp
        self.name = name
        self.img = img
        self.price = price


class USER(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    admin = db.Column(db.Boolean)

    def __init__(self, username, password, email, phone, admin):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.admin = admin







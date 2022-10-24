from utils.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    money = db.Column(db.Integer())
    
    
def __init__(self,nombre,money):
    self.nombre = nombre
    self.money = money
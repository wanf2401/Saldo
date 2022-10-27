
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts',__name__)

@contacts.route("/")
def index():
    return render_template('index.html')

@contacts.route('/new')
def new_contact():
        return render_template('commit.html')

@contacts.route("/register")
def register_contact():
    
        #nombre = request.form['nombre']
        #nombre1 = request.form['nombre1']
        #Apellido = request.form['Apellido']
        #Apellido1 = request.form['Apellido1']
        #email = request.form['email']
        #phone = request.form['phone']
        
        #new_contact = Contact(nombre,nombre1,Apellido,Apellido1,email,phone)

        #db.session.add(register_contact)
        #db.session.commit()
        
    return render_template('register.html')

@contacts.route("/saldo")
def saldo_contact():
    return render_template('saldo.html')

@contacts.route("/password")
def password_contact():
    
        #correo = request.form['correo']
        
        #new_contact = Contact(correo)

        #db.session.add(register_contact)
        #db.session.commit()
    
    return render_template('password.html')

@contacts.route("/login")
def update_contact():
    return render_template('commit.html')
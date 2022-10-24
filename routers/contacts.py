
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts',__name__)

@contacts.route("/")
def index():
    return render_template('index.html')

@contacts.route('/new', methods=['POST'])
def new_contact():
        nombre = request.form['nombre']
        money = request.form['money']
        
        new_contact = Contact(nombre, money)

        db.session.add(new_contact)
        db.session.commit()

        return "SALVO INFO"

@contacts.route("/update")
def update_contact():
    return "saldo Actualizado guardado"
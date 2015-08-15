from flask import Blueprint, render_template
from tiles import tiles

hedgehog = Blueprint('hedgehog', __name__)


@hedgehog.route('/')
@hedgehog.route('/home')
def home():
    return render_template('home.html', tiles=tiles)


@hedgehog.route('/login')
def login():
    print(tiles)
    return render_template('login.html', tiles=tiles)

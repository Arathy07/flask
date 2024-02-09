from flask import *
from database import *
user=Blueprint('user',__name__)
@user.route('/')
def home():
    return render_template("home.html")


@user.route('/userlogin')
def login():
    return render_template("userlogin.html")


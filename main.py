from flask import *
from public import*


app=Flask(__name__)
app.register_blueprint(public)
app.run(port=5002,debug=True)

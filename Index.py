#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)#object

@app.route('/')#wrap
def index():#function
    return 'this is my first server'#return string
app.run()#run server port 5000

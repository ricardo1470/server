#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/client')
def client():
    list_name = ['client1', 'client2', 'client3', 'client4']
    return render_template("client.html", list=list_name)

@app.route('/params')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name = "value", num = "nothing"):
    return ('the parameter is: {} {}'.format(name, num))

if __name__ == '__main__':
    app.run(debug= True, port=9000)#run server port 9000

#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

"""@app.route('/params')
def params():
    param = request.args.get('params1', 'it has no parameters')
    return 'the parameter is: {}'.format(param)"""

@app.route('/params')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name = "value", num = "nothing"):
    return ('the parameter is: {} {}'.format(name, num))

if __name__ == '__main__':
    app.run(debug= True, port=9000)#run server port 9000
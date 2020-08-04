#!/usr/bin/python3
from flask import Flask
from flask import render_template
import forms 

app = Flask(__name__)#object

@app.route('/')#wrap
def index():#function
    comment_form = forms.comment_form()
    title = "my form"
    return render_template('index.html', title = title, form = comment_form)

if __name__ == '__main__':
    app.run(debug= True, port=9000, host='127.0.0.1')#run server port 9000

#!/usr/bin/python3
"""create class"""
from wtforms import Form
from wtforms import StringField, TextFiel
from wtforms.fields.html5 import EmailField


class CommentForm(Form):
    """init class Form"""
    username = StringField('username')
    email = EmailField('email')
    comment = TextFiel('comment')

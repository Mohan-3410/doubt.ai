# user.js should actually be named user.py if it's a Python file
from mongoengine import Document, StringField, EmailField, DictField

class User(Document):  # Capitalize the class name to follow Python conventions
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    name = StringField(required=True)
    avatar = DictField()  # Optional dictionary for storing avatar data

    meta = {
        'collection': 'users',
        'indexes': [{'fields': ['email'], 'unique': True}],
        'ordering': ['-created_at']
    }

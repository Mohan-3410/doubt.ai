from flask import Flask
from dotenv import load_dotenv
from dbConnect import db
from controller.auth_controller import auth
from controller.bot_controller import bot
from flask_jwt_extended import JWTManager
from datetime import timedelta

load_dotenv()  

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to your secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=365)
JWTManager(app)
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(bot, url_prefix='/bot')
db()

@app.route('/')

def welcome():
    return 'Welcome to doubtme.ai'

@app.route('/home')
def home():
    return 'Welcome to Home'

from controller import *






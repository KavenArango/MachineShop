from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
Bootstrap(app)
login_manager = LoginManager(app)
app.config['SECRET_KEY'] = 'KILLME'




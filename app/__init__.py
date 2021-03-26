from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '91cb01075fbd0824e7d3c425b55ba2ae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['CLASS8_NOTES'] = 'app/static/notes/CLASS8_NOTES'
app.config['CLASS9_NOTES'] = 'app/static/notes/CLASS9_NOTES'
app.config['CLASS10_NOTES'] = 'app/static/notes/CLASS10_NOTES'
app.config['CLASS11_NOTES'] = 'app/static/notes/CLASS11_NOTES'
app.config['CLASS12_NOTES'] = 'app/static/notes/CLASS12_NOTES'
db = SQLAlchemy(app) 
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
socketio = SocketIO(app)

from app import routes
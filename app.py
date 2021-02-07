from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cle_secrete'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

from routes import *   # rapporte l'ensemble du code dans routes-py

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0')

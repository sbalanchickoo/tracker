from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialize app
app = Flask(__name__)


# initialize db
username = "postgres"
password = "gt"
dbname = "tracker"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:gt@localhost:5432/tracker"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# db.create_all()
from string import ascii_lowercase
from random import choice

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Link(db.Model):

    __tablename__ = "links"

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(150))
    token = db.Column(db.String(20), index=True)
    visits = db.Column(db.Integer, default=0)

    def set_shortcut(self):

        self.token = "".join([choice(ascii_lowercase) for _ in range(5)])

    def add_visits(self):
        self.visits += 1

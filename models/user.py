import sqlite3
from db import db


class UserModel(db.Model):
    """
    Create the user object.
    """

    # TELL SQLAlchemy THE TABLE NAME:
    __tablename__ = 'users'

    # HOW MANY COLUMNS TO CONTAIN:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        """
        Initialize the class.
        """
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        """
        Find a user in the database searching by the username.
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        """
        Find a user in the database searching by the id.
        """
        return cls.query.filter_by(id=_id).first()
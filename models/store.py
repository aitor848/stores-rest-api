from db import db


class StoreModel(db.Model):
    """
    This is the store-model.
    """

    # TELL SQLAlchemy THE TABLE NAME:
    __tablename__ = 'stores'

    # HOW MANY COLUMNS TO CONTAIN:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')


    def __init__(self, name):
        """
        Initialize the class.
        """
        self.name = name

    def json(self):
        """
        Return a json representation of the model; a dictionary.
        """
        return {
            'name': self.name,
            'items': [item.json() for item in self.items.all()]
            }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        """
        Save the model into the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Delete the model of the database.
        """
        db.session.delete(self)
        db.session.commit()
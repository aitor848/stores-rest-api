from db import db


class ItemModel(db.Model):
    """
    This is the item for models; our internal representation.
    """

    # TELL SQLAlchemy THE TABLE NAME:
    __tablename__ = 'items'

    # HOW MANY COLUMNS TO CONTAIN:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')


    def __init__(self, name, price, store_id):
        """
        Initialize the class.
        """
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        """
        Return a json representation of the model; a dictionary.
        """
        return {'name': self.name, 'price': self.price}

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
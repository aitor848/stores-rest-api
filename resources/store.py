from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        """
        Retrieve a store from the database.
        """
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found!'}, 404

    def post(self, name):
        """
        Create a new store.
        """
        if StoreModel.find_by_name(name):
            return {'message': f'A store with name {store} already exists.'}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            {'message': 'An error occurred creating the store.'}, 500

        return store.json(), 201

    def delete(self, name):
        """
        Delete an existing store.
        """
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store successfully deleted!'}


class StoreList(Resource):
    """
    Make the whole list of stores in our project.
    """
    def get(self):
        """
        Show how many stores we have.
        """
        return {'stores': [store.json() for store in StoreModel.query.all()]}


import os

from flask import Flask
from flask_restful import Api
# For authentication JWT:
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'aitor'
api = Api(app)

# /auth:
jwt = JWT(app, authenticate, identity)

# CREATE THE ENDPOINTS:
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

# RUN APP:
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
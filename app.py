from flask import Flask
from flask_restful import Resource,Api,reqparse
from secret import secret


from resources.item import Item,ItemList
from flask_jwt import JWT, jwt_required
from security import authenticate,identity
from resources.user import UserRegister
from resources.store import Store,StoreList

app = Flask(__name__)


# first set the secret key
app.secret_key = secret

#Configurations for SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#Initialize api
api = Api(app)



#Initialize the JWT
jwt = JWT(app,authenticate,identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store is None:
            return {'message': 'No store named {} present in the database'.format(name)},404
        else:
            return store.json()

    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': 'Store named {}  already exists in the database'.format(name)},400
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {'message':'Could not save to database'},500
            return {'message' : 'Saved to database succesfully!'}

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store is None:
            return {'message': 'No store named {} present in the database'.format(name)},400
        else:
            store.delete_from_db()
            return {'message' : 'Deleted from database succesfully'}

class StoreList(Resource):
    def get(self):
        return {'stores' : [store.json() for store in StoreModel.query.all()]}

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = float,
    required = True,
    help='This field cannot be left blank!'
    )
    parser.add_argument('store_id',
    type = float,
    required = True,
    help='Every utem needs a store id!'
    )
    
    @jwt_required()
    def get(self, _id):
        #next gibt den ersten Werte, der gefunden wurde
        item = ItemModel.find_by_id(_id)
        
        if item:
            return item.json()
        return {'message': 'Item not found.'}, 404  
    
    def post(self,_id):
        
        item = ItemModel.find_by_id(_id)
        if item:
            return{'message': "An Item with id {}' alread exists.".format(_id)}, 400
                        
        data = Item.parser.parse_args()
        item  = ItemModel(_id, data['price'], data['store_id'])
        
        item.insert_item()
            
        return item.json(),201
        
    def delete(self,_id):
        item = ItemModel.find_by_id(_id)
        
        if item is None:
            return {'message':'Item does not exist.'}
        item.delete_from_db()
        
        return {'message':'Item deleted'}
        
    def put(self, _id):
        
        data = Item.parser.parse_args()        
        item = ItemModel.find_by_id(_id)
        
        if item is None:
            item = ItemModel(_id, data['price'],data['store_id'])
            msg = 'Item {} is created.'.format(_id)
            
        
        item.price = data['price']
        item.store_id = data['store_id']
        msg = 'Item {} is updated.'.format(_id)
            
        item.insert_item()
        return {'message':msg}
        
        
class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
        
      

        

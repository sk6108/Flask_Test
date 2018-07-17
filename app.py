from flask import Flask
from flask_restful import Api, reqparse
from flask_jwt import JWT
from security import autheticate, identity
from resources.user import UserRegister, UserList
import sqlite3
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.secret_key = 'sk'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, autheticate, identity) #/auth
        
api.add_resource(Item,'/item/<string:_id>')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(ItemList,'/items/')
api.add_resource(StoreList,'/stores/')
api.add_resource(UserRegister,'/register')
api.add_resource(UserList,'/userList')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
import sqlite3
from db import db

class ItemModel(db.Model):
    
    __tablename__ = 'items'
    
    RowID = db.Column(db.Integer,primary_key = True)
    id = db.Column(db.Integer)
    price = db.Column(db.Float(precision = 2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    
    def __init__(self, _id, price,store_id):
        self.id = _id
        self.price = price
        self.store_id = store_id
        
    def json(self):
        return {'id': self.id, 'price': self.price, 'store_id': self.store_id}
        
    @classmethod
    def find_by_id(cls, _id ):
        return cls.query.filter_by(id = _id).first()
        
    def insert_item(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
  
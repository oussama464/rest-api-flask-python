from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(
        db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False
    )
    # so i can use myitme.store and get a store object -- backpopulates = item so that the store model have an items variable so that i can do store.items
    store = db.relationship("StoreModel", back_populates="items")

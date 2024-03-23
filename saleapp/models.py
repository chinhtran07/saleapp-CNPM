from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from saleapp import db, app
from flask_login import UserMixin


class Category(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Float, default=0.0)
    image = Column(String(150), default='')
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        # link = "https://cdn-v2.didongviet.vn/files/products/2023/6/14/1/1689351170740_samsung_galaxy_z_flip4_didongviet_1.jpg"
        # print(link.__len__())
        import json

        with open("data/products.json", encoding="utf-8") as f:
            products = json.load(f)

            for p in products:
                prod = Product(**p)
                db.session.add(prod)

        db.session.commit()

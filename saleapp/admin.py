from flask_admin import Admin, BaseView
from flask_admin.contrib.sqla import ModelView

from saleapp import app, db
from saleapp.models import Category, Product


class ProductModelView(ModelView):
    column_list = ['id', 'name', 'category_id']
    column_filters = ['id', 'name']


class CategoryModelView(ModelView):
    column_list = ['id', 'name', 'products']


class StatsView(BaseView):



admin = Admin(app, name="E_Commerce", template_mode="bootstrap4")
admin.add_view(ProductModelView(Product, db.session))
admin.add_view(CategoryModelView(Category, db.session))

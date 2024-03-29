import math

from flask import render_template, request, redirect
import dao
from saleapp import app, admin


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    page = request.args.get('page')
    categories = dao.load_categories()
    products = dao.load_products(q, cate_id, page)
    return render_template("index.html", categories=categories, products=products, pages=math.ceil(dao.count_products()/app.config['PAGE_SIZE']))


@app.route("/products/<int:id>")
def detail(id):
    product = dao.get_product_by_id(id)
    return render_template("product_detail.html", product=product)


@app.route('/login', methods=['get', 'post'])
def login_my_user():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        if username.__eq__('admin') and password.__eq__('123'):
            return redirect('/')

    return render_template('login.html')


@app.context_processor
def common_attributes():
    return {
        'categories': dao.load_categories()
    }


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

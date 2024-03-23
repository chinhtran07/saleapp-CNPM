from saleapp.models import Product, Category, User
from saleapp import app, login


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def load_categories():
    cates = Category.query.all()
    return cates


def count_products():
    return Product.query.count()


def load_products(q, cate_id, page=None):
        query = Product.query

        if q:
            query = query.filter(Product.name.contains(q))

        if cate_id:
            query = query.filter(Product.category_id.__eq__(cate_id))
        if page:
            page_size = app.config["PAGE_SIZE"]
            start = (int(page) - 1) * page_size
            query = query.slice(start, start + page_size)

        return query.all()


def get_product_by_id(product_id):
        product = Product.query.get(product_id)

        return product



if __name__ == "__main__":
    with app.app_context():
        print(load_categories())


from flask import Flask, render_template, request, url_for, redirect, jsonify
from table import *


app = Flask(__name__)


# đường dẫn tới data base trên postgres
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:12345@localhost:5432/mydata"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

# todo được sử dụng để khởi tạo extension của cơ sở dữ liệu trong ứng dụng Flask
db.init_app(app)

#! -- hiển thị page


@app.route("/")
def trangchu1():
    food = FOOD.query.all()
    return render_template("home.html", foods=food)


@app.route("/home")
def trangchu():
    food = FOOD.query.all()
    return render_template("home.html", foods=food)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/page", methods=['POST', 'GET'])
def page():
    value = request.form['next_page']
    if value in "Danh sách món ăn":
        return redirect(url_for("food"))
    elif value in "Danh sách đơn hàng":
        return redirect(url_for("order"))
    else:
        return

#! --- xử lý form


def create():
    # todo:  tạo bảng
    db.create_all()


# ---- thêm dũ liệu vào bảng

def data():
    #  data  sản phẩm  mẫu
    f = open('E:\WEB FLASK\\food.csv', encoding="UTF-8")
    data = csv.reader(f)

    next(data)  # Bỏ qua hàng đầu tiên chứa tiêu đề cột

    for msp, name, img, price in data:
        food = FOOD(msp=f"{msp.strip()}", name=f"{name.strip()}", img=f'{img.strip()}',
                    price=price.strip())
        db.session.add(food)
        db.session.commit()

#   ---- BOOK -----
# todo: INSERT


@app.route('/book', methods=['POST', 'GET'])
def submit_form_book():
    product = request.form['product']
    price = request.form['price']
    number = request.form['number']
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']

    sum_price = 0
    for i in range(int(number)):
        sum_price += int(price)

    book = BOOK(product=f'{product}', price=sum_price, number=f'{number}',
                name=f'{name}', address=f'{address}', phone=f'{phone}', email=f'{email}')
    # -- lệnh thêm vào
    db.session.add(book)
    #  -- lệnh lưu thay đổi
    db.session.commit()
    return redirect(url_for("trangchu"))


# todo : SELECT

@app.route("/admin/order")
def order():
    book = BOOK.query.all()
    return render_template("order.html", books=book)


# todo : delete
@app.route('/delete_order/<int:id>')
def delete_user(id):
    user_to_delete = BOOK.query.get(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    db.session.delete(user_to_delete)
    return redirect(url_for("order"))


# todo : update
@app.route('/update_order/<int:id>')
def update_order(id):
    book = BOOK.query.get(id)
    return render_template("form_update_order.html", books=book)


@app.route('/update_order_user', methods=["post", "get"])
def update_order_user():
    # lấy stt để update
    id = request.form['id']
    product = request.form['product']
    price = request.form['price']
    number = request.form['number']
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    # ---
    user_update = BOOK.query.get(id)
    user_update.product = product
    user_update.price = price
    user_update.number = number
    user_update.name = name
    user_update.address = address
    user_update.phone = phone
    user_update.email = email

    db.session.commit()
    return redirect(url_for('order'))


# todo : tìm kiếm


@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    results = []
    data = BOOK.query.filter(BOOK.name.like(f'%{keyword}%')).all()

    if data == "":
        print()
    else:
        for i in data:
            r = {"id": f'{i.id}', "name": f'{i.name}',
                 "product": f'{i.product}', "price": f'{i.price}', "number": f'{i.number}', "phone": f'{i.phone}', "email": f'{i.email}', }
            results.append(r)

    return jsonify(results)


#   ---- FOOD -----
# todo : INSERT


@app.route('/food', methods=['POST', 'GET'])
def submit_form_food():
    msp = request.form['msp']
    name = request.form['name']
    img = request.form['img']
    price = request.form['price']

    food = FOOD(msp=f"{msp}", name=f"{name}", img=f'{img}',
                price=price)
    # -- lệnh thêm vào
    db.session.add(food)
    #  -- lệnh lưu thay đổi
    db.session.commit()
    return redirect(url_for("food"))

# todo  : SELECT


@app.route("/admin/food")
def food():
    food = FOOD.query.all()

    return render_template("food.html", foods=food)

# todo : delete


@app.route('/delete_food/<int:id>')
def delete_food(id):
    user_to_delete = FOOD.query.get(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    db.session.delete(user_to_delete)
    return redirect(url_for("food"))

# todo : update


@app.route('/update_food/<int:id>')
def update_food(id):
    food = FOOD.query.get(id)
    return render_template("form_update_food.html", foods=food)


@app.route('/update_food_user', methods=["post", "get"])
def update_food_user():
    # lấy stt để update
    id = request.form['id']
    msp = request.form['msp']
    name = request.form['name']
    img = request.form['img']
    price = request.form['price']
    # ---
    user_update = FOOD.query.get(id)
    user_update.msp = msp
    user_update.name = name
    user_update.img = img
    user_update.price = price

    db.session.commit()
    return redirect(url_for('food'))


if __name__ == "__main__":
    with app.app_context():
        # create()
        # data()
        app.run(debug=True)

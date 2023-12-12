from flask import Flask, render_template,request,url_for,redirect,session,flash



app = Flask(__name__)
app.config["SECRET_KEY"] = "Vanh"

@app.route("/")
def index():
    return render_template("index.html")    


# comment
@app.route("/login" , methods=["POST","GET"])
def login():
    if request.method == "POST":
        user_name = request.form["txt_name"]
        session["user"] = user_name
        return redirect(url_for("trangchu"))
    else:
        return render_template("login.html")


@app.route("/user")
def home():
    if "user" in session:
        name = session["user"]
        return render_template("home.html", context=name)

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
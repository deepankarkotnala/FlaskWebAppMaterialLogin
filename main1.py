from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

#app.secret_key = os.urandom(12)
app.secret_key = os.environ.get('SECRET')

@app.route("/")
def home():
    if not session.get("logged_in"):
        return render_template("login_page.html", title="Login")
    else:
        return render_template("home.html", title="Home")

@app.route("/login", methods=["POST"])
def do_admin_login():
    if session.get("logged_in"):
        return render_template("home.html", title="Home")
    if request.form["password"] == "password" and request.form["username"] == "admin":
        session["logged_in"] = True
        return render_template("home.html", title ="Home")
    else:
        flash("wrong password!")
        return home()


@app.route("/logout")
def logout():
    session["logged_in"] = False
    return home()


@app.route("/signup")
def signup():
    return render_template("signup_page.html", title="Signup")


@app.route("/about")
def about():
  return render_template("about.html", title="About Us")


if __name__ == "__main__":
    app.run(debug=True)

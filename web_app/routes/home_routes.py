from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")

@home_routes.route("/seasonality")
def seasonality():
    print("Seasonality...")
    return render_template("seasonality.html")

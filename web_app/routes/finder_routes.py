from flask import Blueprint, request, render_template, redirect, flash
import pandas as pd

finder_routes = Blueprint("finder_routes", __name__)

@finder_routes.route("/finder", methods=["GET","POST"])
def finder():
    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    user_city = form_data["userCity"]
    user_state = form_data["userState"]

    exported_csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR1bQD0eLLXftfkcHn_8bujOYp6jG162KBuBrA59wLMw6MSByA3R1snZm49IyhuF822LcwL6A1ICP_S/pub?output=csv"
    df = pd.read_csv(exported_csv_url, on_bad_lines='skip')

    filtered_markets = df[(df["market_city"] == user_city) & (df["market_state"] == user_state)]
    market_list = []

    if not filtered_markets.empty:
        print("The following farmers markets are available in", user_city + ",", user_state, ":")
        for index, row in filtered_markets.iterrows():
            market_list.append(dict(row))
    else:
        market_list.append("No farmers markets found in {} {}".format(user_city, user_state))
        print(f"No farmers markets found in {user_city} {user_state}")

    return render_template("finder.html", market_list=market_list)
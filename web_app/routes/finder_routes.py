from flask import Blueprint, request, render_template, redirect, flash
import pandas as pd

finder_routes = Blueprint("finder_routes", __name__)

@finder_routes.route("/finder")

exported_csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR1bQD0eLLXftfkcHn_8bujOYp6jG162KBuBrA59wLMw6MSByA3R1snZm49IyhuF822LcwL6A1ICP_S/pub?output=csv"  # Replace with the actual URL

df = pd.read_csv(exported_csv_url, on_bad_lines='skip')

filtered_markets = df[(df["market_city"] == user_city) & (df["market_state"] == user_state)]

if not filtered_markets.empty:
    print("The following farmers markets are available in", user_city + ",", user_state, ":")
    for index, row in filtered_markets.iterrows():
        print()
        print("Market Name:", row["market_name"])
        print("Market Address:", row["market_street"] + "", row["market_city"] + ",", row["market_state"], row["market_zip"])
        print("-" * 20)
else:
    print("+ No farmers markets found in", user_city + ",", user_state+". Please enter a new location.")
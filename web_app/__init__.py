from flask import Flask
import os
from dotenv import load_dotenv

from web_app.routes.home_routes import home_routes
from web_app.routes.finder_routes import finder_routes


load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(finder_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
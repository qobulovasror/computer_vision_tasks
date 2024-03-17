from flask import Flask
# from flask.ext.mongoalchemy import MongoAlchemy
from config import Config

# db = MongoAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # db.init_app(app)
    
    # from views import author_bp
    # app.register_blueprint(author_bp)

    return app
from flask import Flask
from config import Config
import os 
from os.path import join, dirname, realpath

ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg', 'tif'}
INPUT_FILENAME = ''

app = Flask(__name__, template_folder='./templates')
app.config.from_object(Config)
app.config['SECRET_KEY'] = ''
app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)), 'uploaded_files')
app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024


from app import routes
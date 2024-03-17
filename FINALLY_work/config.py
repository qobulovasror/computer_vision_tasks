import os

port = int(os.environ.get('PORT', 5500))
class Config:
    DEBUG = True
    SECRET_KEY = 'secret_key'
    HOST='0.0.0.0'

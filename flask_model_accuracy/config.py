import os

class Config:
    SECRET_KEY = os.urandom(24)
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'csv', 'xlsx'}

import os

# get the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = b'\xa2\x8c\x93]\xed\n\xa5\x11\xba\xe0\x9e\xc6\x0f\xcby\x18\xfb M\xf9Q\x03\x87('

# define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)


from pathlib import Path
from dotenv import load_dotenv
import os


BASEDIR = str(Path(__file__).parent.absolute())

load_dotenv('.env')

class Config(object):
    # Flask secret
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or \
        "sqlite:///" + os.path.join(BASEDIR, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


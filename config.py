import os
from dotenv import load_dotenv

load_dotenv()

class DevConfig(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
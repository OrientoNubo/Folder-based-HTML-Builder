from flask_frozen import Freezer
from app import app

def freezerAPP():
    freezer = Freezer(app)
    freezer.freeze()

if __name__ == '__main__':
    freezerAPP()

from app.views.views import app
from app.helpers.db import Database

db = Database()

"""Runs the app"""
if __name__ == '__main__':
    app.run(debug=True)
    db = Database()
    db.create_tables()
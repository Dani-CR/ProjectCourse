#!/usr/bin/env python
# run:
# $ FLASK_APP=mini_app flask run
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSBase, SAFRSAPI
import coverage

db = SQLAlchemy()

class User(SAFRSBase, db.Model):
    """
        description: User description
    """

    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)


def create_api(app, HOST="localhost", PORT=5000, API_PREFIX=""):
    api = SAFRSAPI(app, host=HOST, port=PORT, prefix=API_PREFIX)
    api.expose_object(User)
    user = User(name="test", email="email@x.org")
    print("Starting API: http://{}:{}/{}".format(HOST, PORT, API_PREFIX))


def create_app(config_filename=None, host="localhost"):
    app = Flask("demo_app")
    app.config.update(SQLALCHEMY_DATABASE_URI="sqlite://")
    db.init_app(app)
    with app.app_context():
        db.create_all()
        create_api(app, host)
    return app


host = "localhost"
app = create_app(host=host)

def main():
    try:
        cov = coverage.Coverage()
        cov.start()

        # Simulate some code execution
        #app.run(host=host)
        print("hello")
    finally:
        cov.stop()
        cov.save()
        cov.report()
    #cov.html_report(directory='htmlcov')  # Create an HTML report

if __name__ == "__main__":
    main()

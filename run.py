from flask import Flask
from app import create_app
from app.seed import seed_data
from app.extensions import db


app = create_app()
app.config["SQLALCHEMY_ECHO"] = True

seed_data(app) # Seed default data

if __name__ == "__main__":
    app.run(port=5000)

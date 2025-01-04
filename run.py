from flask import Flask
from app import create_app
from app.seed import seed_data
from app.seed import seed_person_types
from app.extensions import db
from flask_cors import CORS

app = Flask(__name__)

# with app.app_context():
#     seed_person_types()

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:5173"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

if __name__ == "__main__":
    app.run(port=5000)

app.get('/',)
from app import create_app
from app.seed import seed_data
from app.seed import seed_person_types
from app.extensions import db

app = create_app()

# with app.app_context():
#     seed_person_types()

if __name__ == "__main__":
    app.run(debug=True)

app.get('/',)
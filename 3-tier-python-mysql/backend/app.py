import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define the path for the SQLite database file
# It will be created in the same directory as this script.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'countries.db')

# --- Flask App Setup (Minimal, just for SQLAlchemy context) ---
# We create a Flask app instance here primarily to provide the
# application context necessary for SQLAlchemy to interact with the database.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# -----------------------------------------------------------

# Define the Country model (same as in your Flask app)
class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    capital = db.Column(db.String(100), nullable=False)
    currency = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Country {self.name}>'

    def to_dict(self):
        return {
            'country': self.name,
            'capital': self.capital,
            'currency': self.currency
        }

# Function to initialize the database schema (does not populate data)
def init_db():
    db_exists = os.path.exists(DATABASE_PATH)
    if not db_exists:
        print(f"Database file '{DATABASE_PATH}' not found. Creating a new one.")
        db.create_all() # Create tables defined by models
        print("Database tables created. Please ensure data is loaded into 'countries.db' externally.")
    else:
        print(f"Database file '{DATABASE_PATH}' already exists. Skipping creation.")
        # If the DB exists, the script now assumes data is present or will be loaded externally.

# Main execution block
if __name__ == '__main__':
    # Ensure we are within a Flask application context for DB operations
    with app.app_context():
        # Initialize (create if needed) the database schema
        init_db()

        # Read data from the database
        print("\n--- Reading data from countries.db ---")
        all_countries = Country.query.all()
        if all_countries:
            for country in all_countries:
                print(f"Country: {country.name}, Capital: {country.capital}, Currency: {country.currency}")
        else:
            print("No data found in the database. Please populate the database externally if this is unexpected.")
        print("--------------------------------------")

    print("\nScript finished. The 'countries.db' file should now exist in this directory (if it didn't before).")
    print("You can now run your Flask app (app.py) which will use this database.")

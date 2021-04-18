from app import app
from db import db

db.init_app(app)

# Flask decorator; it's going to affect the method below it. 
## (It is going to run this method before the first request.)
@app.before_first_request
def create_tables():
    """
    Tell SQLAlchemy to create the tables.
    """
    db.create_all()
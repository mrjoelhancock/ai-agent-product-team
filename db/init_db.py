# db/init_db.py

from db.database import Base, engine
from db import models  # This must import your model definitions

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database schema created.")

if __name__ == "__main__":
    init_db()
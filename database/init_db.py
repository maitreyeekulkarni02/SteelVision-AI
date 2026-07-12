"""
Initialize SteelVision AI Database
"""


from database.database import engine, Base

from database.models import InspectionHistory



print("Creating database tables...")


Base.metadata.create_all(
    bind=engine
)


print("Database ready!")
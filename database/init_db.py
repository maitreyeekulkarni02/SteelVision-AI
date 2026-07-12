"""
SteelVision AI
Database Initialization
"""


from database.database import engine, Base

from database.models import InspectionHistory

from database.machine_models import Machine



print(
    "Creating database tables..."
)



Base.metadata.create_all(
    bind=engine
)



print(
    "Database ready!"
)
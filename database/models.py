"""
SteelVision AI
Database Models

Stores machine inspection records.
"""

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from database.database import Base


class InspectionHistory(Base):
    """
    Industrial inspection history table
    """

    __tablename__ = "inspection_history"

    id = Column(Integer, primary_key=True, index=True)

    machine_name = Column(String, default="Machine-01")

    inspection_time = Column(DateTime, default=datetime.utcnow)

    defects = Column(Text)

    health_score = Column(Float)

    machine_status = Column(String)

    maintenance_priority = Column(String)

    recommendation = Column(Text)

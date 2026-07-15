"""
SteelVision AI
Machine Database Model

Stores industrial machine information.
"""

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from database.database import Base


class Machine(Base):
    """
    Industrial Machine Registry
    """

    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)

    machine_id = Column(String, unique=True, index=True)

    machine_name = Column(String)

    machine_type = Column(String)

    location = Column(String)

    installation_date = Column(String)

    current_health = Column(Float, default=100)

    last_inspection = Column(DateTime, default=datetime.utcnow)

    status = Column(String, default="Unknown")

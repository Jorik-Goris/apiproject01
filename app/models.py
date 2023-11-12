from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(255), index=True)
    temperature = Column(Float)
    conditions = Column(String(255))
    precipitation = Column(Boolean)

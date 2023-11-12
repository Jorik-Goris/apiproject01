from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas


def get_weather(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weather).offset(skip).limit(limit).all()

def create_weather(db: Session, weather: schemas.WeatherCreate, city: str):
    db_weather = models.Weather(city=city, temperature=weather.temperature, conditions=weather.conditions,
                                precipitation=weather.precipitation)
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather

def get_weather_by_city(db: Session, city: str):
    return db.query(models.Weather).filter(models.Weather.city == city).first()

def delete_weather(db: Session, weather: models.Weather):
    db.delete(weather)
    db.commit()
    return weather

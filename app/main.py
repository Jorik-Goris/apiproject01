from fastapi import Depends, FastAPI, HTTPException, status, Depends, Header
import requests
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import schemas
import crud
import models
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to a specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
if not openweather_api_key:
    raise EnvironmentError("OpenWeather API key not found in environment variables.")

api_keys = {
    "ABC": {"owner": "user1"},
    "DEF": {"owner": "user2"},
}

def get_api_key(api_key: str = Header(...)):
    if api_key not in api_keys:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key


# Apply get_api_key globally
app = FastAPI(dependencies=[Depends(get_api_key)])


@app.get("/weather/{city}")
def get_weather(city: str):
    # Define the URL for the OpenWeather API request
    openweather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}'

    # Make the HTTP request to the OpenWeather API
    response = requests.get(openweather_url)

    # Check if the request to the OpenWeather API was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response to access weather data
        weather_data = response.json()

        # Extract temperature in Kelvin
        temperature_kelvin = weather_data.get('main', {}).get('temp', None)

        # Convert Kelvin to Celsius
        temperature_celsius = temperature_kelvin - 273.15

        conditions = weather_data.get('weather', [{}])[0].get('description', 'Unknown')

        # Return the relevant weather data in Celsius in your FastAPI response
        return {"city": city, "temperature": temperature_celsius, "conditions": conditions}
    else:
        return {"error": "Unable to retrieve weather data."}


#returned kneiters veel data, wa mee doen?
@app.get("/forecast/{city}")
def get_weather_forecast(city: str):
    # Endpoint to retrieve weather forecast data for a specific city

    # Define the URL for the OpenWeather API forecast request
    openweather_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={openweather_api_key}'

    # Make the HTTP request to the OpenWeather API
    response = requests.get(openweather_url)

    if response.status_code == 200:
        forecast_data = response.json()
        # Process the forecast data as needed

        return {"city": city, "forecast_data": forecast_data}
    else:
        raise HTTPException(status_code=404, detail="No forecast data available for the specified city")

# GET endpoint for weather based on city
@app.get("/weatherlocal/{city}", response_model=schemas.Weather)
def read_weather(city: str, db: Session = Depends(get_db)):
    db_weather = crud.get_weather_by_city(db, city=city)
    if not db_weather:
        raise HTTPException(status_code=404, detail="Weather not found")

    return db_weather

# POST endpoint for weather based on city
@app.post("/weatherlocal/{city}", response_model=schemas.Weather)
def create_weatherlocal(city: str, weather: schemas.WeatherCreate, db: Session = Depends(get_db)):
    # Check if the weather already exists
    db_weather = crud.get_weather_by_city(db, city=city)
    if db_weather:
        # If weather already exists, return it without creating a new record
        return db_weather

    # If weather doesn't exist, create a new record
    return crud.create_weather(db=db, weather=weather, city=city)



# DELETE endpoint for weather based on city
@app.delete("/weatherlocal/{city}", response_model=schemas.Weather)
def delete_weatherlocal(city: str, db: Session = Depends(get_db)):
    db_weather = crud.get_weather_by_city(db, city=city)
    if not db_weather:
        raise HTTPException(status_code=404, detail="Weather not found")

    crud.delete_weather(db=db, weather=db_weather)
    return db_weather

from pydantic import BaseModel

class WeatherBase(BaseModel):
    city: str
    temperature: float
    conditions: str
    precipitation: bool | None = None


class WeatherCreate(WeatherBase):
    pass

class Weather(WeatherBase):
    city: str
    temperature: float
    conditions: str
    precipitation: bool | None = None

    class Config:
        orm_mode = True
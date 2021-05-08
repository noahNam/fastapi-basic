from fastapi import FastAPI, requests
from pydantic import BaseModel

app = FastAPI()

db = []


class City(BaseModel):
    name: str
    timezone: str


@app.get("/")
def main():
    return {"Hello": "World"}


@app.get("/cities")
def get_cities():
    results = []
    for city in db:
        str_ = f"https://worldtimeapi.org/timezone/{city['timezone']}"
        r = requests.get(str_)
        current_time = r.json()["datetime"]
        results.append({"name": city["name"], "timezone": city["timezone"], "current_time": current_time})

    return results


@app.get("/cities/{city_id}")
def get_city(city_id: int):
    city = db[city_id - 1]
    str_ = f"https://worldtimeapi.org/timezone/{city['timezone']}"
    r = requests.get(str_)
    current_time = r.json()["datetime"]

    return {"name": city["name"], "timezone": city["timezone"], "current_time": current_time}


@app.get("/cities")
def create_city(city: City):
    db.append(city.dict())
    return db[-1]


@app.get("/cities/{city_id")
def delete_city(city_id: int):
    pass

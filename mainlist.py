import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import requests

app = FastAPI()

db = []


# -----------------------------------------------------
# data model
# -----------------------------------------------------
class City(BaseModel):
    name: str
    timezone: str


class CityModify(BaseModel):
    id: int
    name: str
    timezone: str


templates = Jinja2Templates(directory="templates")


@app.get("/")
def main():
    return {"Hello": "World"}


@app.get("/cities", response_class=HTMLResponse)
def get_cities(request: Request):
    context = {}
    result_cities = []

    cnt = 0
    for city in db:
        str_ = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(str_)
        current_time = r.json()['datetime']

        cnt += 1

        result_cities.append(
            {"id": cnt, "name": city["name"], "timezone": city["timezone"], "current_time": current_time})

    context['request'] = request
    context['result_cities'] = result_cities

    return templates.TemplateResponse('city_list.html', context)


@app.get("/cities/{city_id}")
def get_city(city_id: int):
    city = db[city_id - 1]
    str_ = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
    r = requests.get(str_)
    current_time = r.json()["datetime"]

    return {"name": city["name"], "timezone": city["timezone"], "current_time": current_time}


@app.post("/cities")
def create_city(city: City):
    db.append(city.dict())
    return db[-1]


@app.put("/cities")
def modify_city(city: CityModify):
    db[city.id - 1] = {"name": city.name, "timezone": city.timezone}
    return db[city.id - 1]


@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id - 1)

    return {'result_msg': 'Deleted...'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

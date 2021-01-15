"""
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

db=[{"delhi":"Ist"}]

class city(BaseModel):
    name: str
    time_zone: str


@app.get('/')
def index():
    return {'key':'value'}

@app.get('/cities')   
def get_cities():
    return db


@app.get('/cities/{city_id}') 
def get_city(city_id: int):
    return db[city_id-1]

@app.post('/cities')
def create_city(ci: city):
    db.append(ci.dict())
    return db[-1]


@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)
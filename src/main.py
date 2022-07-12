
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db
import models
import schemas
import crud

import uvicorn

app = FastAPI()

@app.get("/")
def getData():
    return {"HELLO": "greeting"}

@app.get("/trend", response_model=List[schemas.TrendPublic])
def get_all_trend(db: Session = Depends(get_db)):
    db_trend = crud.get_all_trend(db=db)
    if db_trend is None:
        raise HTTPException(status_code=404, detail="trend not found")
    return db_trend

@app.get("/trend/ranking/{ranking}", response_model=List[schemas.TrendPublic])
def get_ranking(ranking: int, db: Session = Depends(get_db)):
    db_trend = crud.get_ranking(db=db, ranking=ranking)
    if db_trend is None:
        raise HTTPException(status_code=404, detail="Trend not found")
    return db_trend

@app.get("/trend/top3/JP", response_model=List[schemas.TrendPublic])
def get_top3_JP(db: Session = Depends(get_db)):
    db_trend = crud.get_top3_JP(db=db)
    if db_trend is None:
        raise HTTPException(status_code=404, detail="Trend not found")
    return db_trend

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
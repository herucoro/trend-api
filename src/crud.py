from sqlalchemy.orm import Session
import models
import schemas

def get_ranking(db: Session, ranking: int):
    return db.query(models.Trend).filter(models.Trend.ranking == ranking).all()

def get_top3_JP(db: Session):
    return db.query(models.Trend).filter(models.Trend.ranking < 4).filter(models.Trend.country == 'JP').all()

def get_all_trend(db: Session):
    return db.query(models.Trend).all()
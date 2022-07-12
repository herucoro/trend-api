from datetime import datetime
from pydantic import BaseModel

class TrendBase(BaseModel):
    checked_at: datetime
    ranking: int
    name: str
    country: str

    class Config:
        orm_mode = True

class TrendPublic(TrendBase):
    checked_at: datetime
    ranking: int
    name: str
    country: str

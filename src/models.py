from database import Base
import sqlalchemy as sa

class Trend(Base):
    __tablename__ = "trend"
    checked_at = sa.Column("checked_at", sa.DateTime, primary_key=True)
    ranking = sa.Column("ranking", sa.Integer, primary_key=True)
    name = sa.Column("name", sa.VARCHAR(255))
    country = sa.Column("country", sa.VARCHAR(100))
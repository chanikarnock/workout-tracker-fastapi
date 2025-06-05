from sqlalchemy import Column, DateTime, Integer, String, Boolean
import datetime
from app.models.base import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    disabled = Column(Boolean, default=False)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    

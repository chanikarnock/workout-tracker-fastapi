from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import relationship

import datetime
from app.models.db.base import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    disabled = Column(Boolean, default=False)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    workout_plans = relationship(
        "WorkoutsPlan",
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True
    )
    

import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.models.db.base import Base


class ExerciseCategory(enum.Enum):
    STRENGTH = 1
    AEROBIC = 2
    FLEXIBILITY = 3
    BALANCE = 4


class ExerciseOption(Base):
    __tablename__ = "exercise_options"
    exec_op_id = Column(Integer, primary_key=True)
    exec_id = Column(Integer, ForeignKey("exercises.exec_id"))
    option_name = Column(String)
    option_value = Column(String)
    exercise = relationship("Exercise", back_populates="options")
    
    
class Exercise(Base):
    __tablename__ = 'exercises'
    exec_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    category = Column(Enum(ExerciseCategory))
    muscle_group = Column(String, nullable=True)
    options = relationship("ExerciseOption", lazy="joined", back_populates="exercise")



from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.db.users import User
from app.models.db.exercises import Exercise, ExerciseOption
from app.models.db.base import Base



class WorkoutsPlan(Base):
    __tablename__ = 'workouts_plans'
    wp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    start_at = Column(DateTime, nullable=True)
    stop_at = Column(DateTime, nullable=True)
    is_completed = Column(Boolean, default=False)
    completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    exercise_list = relationship("WorkoutExercise", back_populates="workout", cascade="all, delete-orphan")
    
    user = relationship("User", back_populates="workout_plans")


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True, index=True)
    wp_id = Column(Integer, ForeignKey("workouts_plans.wp_id"))
    exec_id = Column(Integer, ForeignKey("exercises.exec_id"))
    selected_option_id = Column(Integer, ForeignKey("exercise_options.exec_op_id"), nullable=True)

    workout = relationship("WorkoutsPlan", back_populates="exercise_list")
    exercise = relationship("Exercise")
    selected_option = relationship("ExerciseOption")

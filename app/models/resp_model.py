from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from app.models.db.exercises import ExerciseCategory


class ExerciseOption(BaseModel):
    exec_op_id: int
    option_name: str
    option_value: str
    
    
class ExerciseResp(BaseModel):
    exec_id: int
    name: str
    description: Optional[str]
    muscle_group: Optional[str]
    category: ExerciseCategory
    options: List[ExerciseOption]


class WorkoutPlanResp(BaseModel):
    wp_id: int
    name: str
    description: Optional[str]
    start_at: datetime
    stop_at: datetime
    created_at: datetime
    is_completed: bool
    completed_at: Optional[datetime]

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, field_validator
from emval import validate_email


class RegisterUserReq(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        try:
            valid_email = validate_email(value)
        except:
            raise ValueError("Invalid email format")
        return valid_email.normalized
    

class LoginUserReq(BaseModel):
    email: str
    password: str
    
        
class UpdateUserReq(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    
    @field_validator("first_name", "last_name")
    def no_empty_strings(cls, v):
        if v == "":
            raise ValueError("Empty strings are not allowed")
        return v

class ExerciseReq(BaseModel):
    exec_id: int
    selected_option_id: Optional[int] = None
    
class CreateWorkoutPlanReq(BaseModel):
    name: str
    description: Optional[str] = None
    start_at: Optional[datetime] = None
    stop_at: Optional[datetime] = None
    exercise_list: List[ExerciseReq]
    
class UpdateWorkoutPlanReq(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_at: Optional[datetime] = None
    stop_at: Optional[datetime] = None
    exercise_list: List[ExerciseReq] = None
    is_completed: Optional[bool] = None
    completed_at: Optional[datetime] = None
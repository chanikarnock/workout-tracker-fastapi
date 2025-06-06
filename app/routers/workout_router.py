from datetime import datetime
from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, Query
from app.interfaces.workout_controller import WorkoutPlanController
from app.models.req_model import CreateWorkoutPlanReq, UpdateWorkoutPlanReq
from app.models.resp_model import ExerciseResp, WorkoutPlanResp
from app.models.db.users import User
from app.routers.dependencies import get_current_active_user

workout_router = APIRouter()


@workout_router.post("/")
async def create_workout_plan(current_user: Annotated[User, Depends(get_current_active_user)],
                              request_body: CreateWorkoutPlanReq):
    return WorkoutPlanController().create_workout_plan(user_id=current_user.id, request_body=request_body)


@workout_router.post("/{plan_id}")
async def update_workout_plan(current_user: Annotated[User, Depends(get_current_active_user)],
                              plan_id: int, request_body: UpdateWorkoutPlanReq):
    return WorkoutPlanController().update_workout_plan(user_id=current_user.id, plan_id=plan_id, request_body=request_body)


@workout_router.delete("/{plan_id}")
async def delete_workout_plan(current_user: Annotated[User, Depends(get_current_active_user)],
                              plan_id: int):
    return WorkoutPlanController().delete_workout_plan(user_id=current_user.id, plan_id=plan_id)


@workout_router.get("/exercise/{exec_id}")
async def get_exercise(exec_id: int) -> ExerciseResp:
    result = WorkoutPlanController().get_exercise(exec_id=exec_id)
    return result


@workout_router.get("/exercise-list")
async def list_all_exercise(exercise_type: Optional[str] = Query(None)) -> List[ExerciseResp]:
    return WorkoutPlanController().list_all_exercise(exercise_type=exercise_type)


@workout_router.get("/workout-list")
async def list_workout_plan(current_user: Annotated[User, Depends(get_current_active_user)]) -> List[WorkoutPlanResp]:
    return WorkoutPlanController().list_workout_plan(user_id=current_user.id)


@workout_router.get("/reports")
async def generate_reports(current_user: Annotated[User, Depends(get_current_active_user)],
                           order: str = Query("desc", pattern="^(asc|desc)$"),
                           start_date: datetime = Query(None),
                           stop_date: datetime = Query(None),
                           is_completed: bool = Query(None)
                           ):
    return WorkoutPlanController().generate_reports(user_id=current_user.id, order=order, start_date=start_date, stop_date=stop_date, is_completed=is_completed)

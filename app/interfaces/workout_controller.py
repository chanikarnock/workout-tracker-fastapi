from datetime import datetime
from typing import Optional
from app.databases.workout_plans_postgres import WorkoutPostgresRepo
from app.usecases.workout.create_workout_use_case import CreateWorkoutPlanUseCase
from app.usecases.workout.delete_workout_use_case import DeleteWorkoutPlanUseCase
from app.usecases.workout.generate_workout_report_use_case import GenerateWorkoutReportUseCase
from app.usecases.workout.get_exercise_use_case import GetExercisePlanUseCase
from app.usecases.workout.list_all_exercise_use_case import ListAllExerciseUseCase
from app.usecases.workout.list_workout_use_case import ListAllWorkoutPlanUseCase
from app.usecases.workout.update_workout_use_case import UpdateWorkoutPlanUseCase


class WorkoutPlanController():
    def __init__(self):
        self.workout_plan_db = WorkoutPostgresRepo()

    def create_workout_plan(self, user_id: int, request_body: dict):
        return CreateWorkoutPlanUseCase(workout_db_repo=self.workout_plan_db).execute(user_id=user_id,
                                                                                      request_body=request_body)

    def update_workout_plan(self, user_id: int, plan_id: int, request_body: dict):
        return UpdateWorkoutPlanUseCase(workout_db_repo=self.workout_plan_db).execute(user_id=user_id, plan_id=plan_id,
                                                                                      request_body=request_body)

    def delete_workout_plan(self, user_id, plan_id: int):
        return DeleteWorkoutPlanUseCase(workout_db_repo=self.workout_plan_db).execute(user_id=user_id,
                                                                                      plan_id=plan_id)

    
    def get_exercise(self, exec_id: int):
        return GetExercisePlanUseCase(workout_db_repo=self.workout_plan_db).execute(exec_id=exec_id)
    
    
    def list_all_exercise(self, exercise_type: str = ""):
        return ListAllExerciseUseCase(workout_db_repo=self.workout_plan_db).execute(exercise_type=exercise_type)
    

    def list_workout_plan(
        self, 
        user_id: int
    ):
        return ListAllWorkoutPlanUseCase(workout_db_repo=self.workout_plan_db).execute(user_id=user_id)


    def generate_reports(
        self,
        user_id: int,
        start_date: Optional[datetime] = None,
        stop_date: Optional[datetime] = None,
        is_completed: Optional[bool] = None,
        order: str = "desc"
    ):
        return GenerateWorkoutReportUseCase(
            workout_db_repo=self.workout_plan_db
        ).execute(
            user_id=user_id,
            order=order,
            start_date=start_date,
            stop_date=stop_date,
            is_completed=is_completed
        )
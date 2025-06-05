from app.databases.workout_plans_postgres import WorkoutPostgresRepo


class UpdateWorkoutPlanUseCase():
    def __init__(self, workout_db_repo: WorkoutPostgresRepo):
        self.workout_repo = workout_db_repo
        pass
    
    def execute(self, user_id: int, plan_id: int, request_body: dict):
        return self.workout_repo.update_workout_plan(user_id=user_id, plan_id=plan_id, request_body=request_body)

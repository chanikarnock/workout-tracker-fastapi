from app.databases.workout_plans_postgres import WorkoutPostgresRepo


class CreateWorkoutPlanUseCase():
    def __init__(self, workout_db_repo: WorkoutPostgresRepo):
        self.workout_repo = workout_db_repo
        pass
    
    def execute(self, user_id: int, request_body: dict):
        result = self.workout_repo.create_workout_plan(user_id=user_id, request_body=request_body)
        return result
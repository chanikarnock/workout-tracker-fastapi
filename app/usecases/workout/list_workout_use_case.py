from app.databases.workout_plans_postgres import WorkoutPostgresRepo


class ListAllWorkoutPlanUseCase():
    def __init__(self, workout_db_repo: WorkoutPostgresRepo):
        self.workout_repo = workout_db_repo
        pass
    
    def execute(self, user_id: int):
        all_exercise = self.workout_repo.list_workout_plan(user_id=user_id)
        return all_exercise
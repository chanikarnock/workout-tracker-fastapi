from app.databases.workout_plans_postgres import WorkoutPostgresRepo


class DeleteWorkoutPlanUseCase():
    def __init__(self, workout_db_repo: WorkoutPostgresRepo):
        self.workout_repo = workout_db_repo
        pass
    
    def execute(self, user_id: int, plan_id: int):
        result = self.workout_repo.delete_workout_plan(user_id=user_id, plan_id=plan_id)
        return result
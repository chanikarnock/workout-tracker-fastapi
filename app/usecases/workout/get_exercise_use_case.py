from app.databases.workout_plans_postgres import WorkoutPostgresRepo


class GetExercisePlanUseCase():
    def __init__(self, workout_db_repo: WorkoutPostgresRepo):
        self.workout_repo = workout_db_repo
        pass
    
    def execute(self, exec_id: int):
        return self.workout_repo.get_exercise(exec_id=exec_id)

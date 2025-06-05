from app.databases.workout_plans_postgres import WorkoutPostgresRepo


class ListAllExerciseUseCase():
    def __init__(self, workout_db_repo: WorkoutPostgresRepo):
        self.workout_repo = workout_db_repo
        pass
    
    def execute(self, exercise_type: str = None):
        if exercise_type:
            exercise_type = exercise_type.split(",")
        all_exercise = self.workout_repo.list_all_exercise(exercise_type=exercise_type)
        return all_exercise
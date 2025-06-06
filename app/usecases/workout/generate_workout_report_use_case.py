from datetime import datetime
from typing import Optional
from app.databases.workout_plans_postgres import WorkoutPostgresRepo


class GenerateWorkoutReportUseCase():
    def __init__(self, workout_db_repo: WorkoutPostgresRepo):
        self.workout_repo = workout_db_repo
        pass

    def execute(
        self,
        user_id: int,
        start_date: Optional[datetime] = None,
        stop_date: Optional[datetime] = None,
        is_completed: Optional[bool] = None,
        order: str = "desc"
    ):
        reports = self.workout_repo.generate_reports(
            user_id=user_id,
            order=order,
            start_date=start_date,
            stop_date=stop_date,
            is_completed=is_completed
        )
        return reports

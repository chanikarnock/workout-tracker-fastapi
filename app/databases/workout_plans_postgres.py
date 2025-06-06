from typing import Optional

from fastapi import HTTPException, status
from app.databases.postgres import PostgresRepo
from app.models.db.exercises import Exercise
from app.models.db.workout_plans import WorkoutExercise, WorkoutsPlan
from app.models.req_model import CreateWorkoutPlanReq
from settings import PG_DB_HOST, PG_DB_NAME, PG_DB_PASS, PG_DB_PORT, PG_DB_USER
from datetime import datetime


class WorkoutPostgresRepo(PostgresRepo):
    def __init__(self):
        super().__init__(
            db_type='postgresql+psycopg2',
            db_host=PG_DB_HOST,
            db_port=PG_DB_PORT,
            db_username=PG_DB_USER,
            db_password=PG_DB_PASS,
            db_name=PG_DB_NAME,
        )


    def list_all_exercise(
        self,
        exercise_type: list[str] = []
    ):
        with self.SessionLocal() as s:
            query = s.query(Exercise)
            if exercise_type:
                query = query.filter(Exercise.category.in_(exercise_type))
            return query.all()
        
        
    def get_exercise(
        self,
        exec_id: int
    ):
        with self.SessionLocal() as s:
            query = s.query(Exercise).filter_by(exec_id=exec_id)
            return query.first()
        

    def create_workout_plan(
        self,
        user_id: int,
        request_body: CreateWorkoutPlanReq
    ):
        with self.SessionLocal() as s:
            new_plan = WorkoutsPlan(
                name=request_body.name,
                description=request_body.description,
                start_at=request_body.start_at,
                stop_at=request_body.stop_at,
                created_by=user_id,
                exercise_list=[],
                created_at=datetime.now()
            )
            exercise_data = request_body.exercise_list
            if exercise_data:
                for ex in exercise_data:
                    new_plan.exercise_list.append(
                        WorkoutExercise(
                            exec_id=ex.exec_id,
                            selected_option_id=ex.selected_option_id
                        )
                    )
            s.add(new_plan)
            s.commit()
            s.refresh(new_plan)
            return new_plan

    
    def update_workout_plan(
        self,
        user_id: int,
        plan_id: int,
        request_body: dict
    ):
        with self.SessionLocal() as s:
            plan = s.query(WorkoutsPlan).filter_by(
                wp_id=plan_id, created_by=user_id).first()
            if not plan:
                raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=str("Workout plan not found")
            )
            updatable_fields = ['name', 'description','is_completed', 'start_at', 'stop_at', 'completed_at']
            for field in updatable_fields:
                if field in request_body:
                    setattr(plan, field, request_body[field])
            if 'exercise_list' in request_body:
                plan.exercise_list.clear()
                s.flush()
                for ex in request_body['exercise_list']:
                    new_ex = WorkoutExercise(
                        exec_id=ex['exec_id'],
                        selected_option_id=ex['selected_option_id']
                    )
                    plan.exercise_list.append(new_ex)
            s.commit()
            s.refresh(plan)
            return plan

    
    def delete_workout_plan(
        self,
        plan_id: int,
        user_id: int
    ):
        with self.SessionLocal() as s:
            target_plan = s.query(WorkoutsPlan).filter_by(
                wp_id=plan_id, created_by=user_id).first()
            if not target_plan:
                raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=str("Workout plan not found")
            )
            s.delete(target_plan)
            s.commit()
        return

    
    def list_workout_plan(
        self,
        user_id: int
    ):
        with self.SessionLocal() as s:
            query = s.query(WorkoutsPlan).filter_by(created_by=user_id).all()
            return query

    
    def generate_reports(
        self,
        user_id: int,
        start_date: Optional[datetime] = None,
        stop_date: Optional[datetime] = None,
        is_completed: Optional[bool] = None,
        order: str = "desc"
    ):
        with self.SessionLocal() as s:
            query = (
                s.query(WorkoutsPlan, Exercise)
                .join(WorkoutExercise, WorkoutExercise.wp_id == WorkoutsPlan.wp_id)
                .join(Exercise, Exercise.exec_id == WorkoutExercise.exec_id)
                .filter(WorkoutsPlan.created_by == user_id)
            )
            if start_date:
                query = query.filter(WorkoutsPlan.created_at >= start_date)
            if stop_date:
                query = query.filter(WorkoutsPlan.created_at <= stop_date)
            if is_completed is not None:
                query = query.filter(WorkoutsPlan.is_completed == is_completed)
            if order == "asc":
                query = query.order_by(WorkoutsPlan.created_at.asc())
            else:
                query = query.order_by(WorkoutsPlan.created_at.desc())
            raw_results = query.all()

            grouped = {}
            for wp, ex in raw_results:
                wp_id = wp.wp_id
                if wp_id not in grouped:
                    grouped[wp_id] = {
                        "workout_plan": {
                            "wp_id": wp.wp_id,
                            "name": wp.name,
                            "created_at": wp.created_at.isoformat(),
                            "is_completed": wp.is_completed
                        },
                        "exercises": []
                    }
                grouped[wp_id]["exercises"].append({
                    "exec_id": ex.exec_id,
                    "name": ex.name
                })
            return grouped

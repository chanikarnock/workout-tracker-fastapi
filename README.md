# workout-tracker-fastapi
Demo Workout Tracker project from roadmap.sh

This project involves creating a backend system for a workout tracker application where users can sign up, log in, create workout plans, and track their progress. The system will feature JWT authentication, CRUD operations for workouts, and generate reports on past workouts.

Tech stack: FastAPI & PostgreSQL

# Setup
1.  Clone the repository:
    
    git clone https://github.com/chanikarnock/workout-tracker-fastapi.git

    
2.  Create and activate a virtual environment:
    
    python3 -m venv .venv
    source  .env/bin/activate
    
3.  Install the dependencies:
    
    pip install -r requirements.txt
    
4.  Set up environment variables, Use the  `.env.example`  file to create a new  `.env`  file with your specific configuration (e.g., database port, JWT secret, etc.).
        
5.  Run the application:
    
    uvicorn main:app

    
 After start, you can use API documentation at  `http://127.0.0.1:8000/docs`.

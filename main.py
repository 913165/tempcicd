import fastapi
from students import students_data

app = fastapi.FastAPI()

# method to get all the students data
@app.get("/students_data")
async def get_students_data():
    return students_data

# method to get students data by student id
@app.get("/students_data/{student_id}")
async def get_students_data(student_id: int):
    for student in students_data:
        if student["student_id"] == student_id:
            return student
    raise fastapi.HTTPException(status_code=404, detail="students_data not found")

# uvicorn command to run the app on port 7000
# uvicorn main:app --reload --port 8000
# command to create requirements.txt
# pip freeze > requirements.txt


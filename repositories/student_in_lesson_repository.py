from db.run_sql import run_sql

from models.student_in_lesson import StudentInLesson
from models.student import Student
from models.lesson import Lesson


import repositories.student_repository as student_repository
import repositories.subject_repository as subject_repository
import repositories.learning_style_repository as learning_style_repository


def save(student_id, lesson_id):
    sql = "INSERT INTO student_in_lesson (student_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [student_id, lesson_id]
    results = run_sql(sql, values)
    result = results[0]['id']
    return result
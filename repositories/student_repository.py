from db.run_sql import run_sql

from models.student import Student
from models.subject import Subject
from models.learning_style import LearningStyle

import repositories.student_repository as student_repository
import repositories.subject_repository as subject_repository
import repositories.learning_style_repository as learning_style_repository


def save(student):
    sql = "INSERT INTO students (first_name, last_name, subject_id, learning_style_id, comment) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [student.first_name, student.last_name, student.subject.subject_id, student.learning_style.id]
    results = run_sql(sql, values)
    student.id = results[0][id]
    return student


def select_all():
    students = []

    sql = "SELECT * FROM students"
    results = run_sql(sql)

    for row in results:
        subject = subject_repository.select(row['subject_id'])
        learning_style = learning_style_repository.select(row['learning_style_id'])
        student = Student(subject, learning_style, row['first_name'], row['last_name'], row['id'], row['comment'])
        students.append(student)
    return student

def select(id):
    student = None
    sql = "SELECT * FROM students WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        for row in result:
            subject = subject_repository.select(row['subject_id'])
            learning_style = learning_style_repository.select(row['learning_style_id'])
        student = Student(subject, learning_style, row['first_name'], row['last_name'], row['id'], row['comment'])
    return student


def delete_all():
    sql = "DELETE FROM students"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM student WHERE id = %s"
    values = [id]
    run_sql(sql, values)


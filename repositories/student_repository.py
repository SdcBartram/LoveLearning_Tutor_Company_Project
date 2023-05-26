from db.run_sql import run_sql

from models.student import Student
from models.subject import Subject
from models.learning_style import LearningStyle

import repositories.student_repository as student_repository
import repositories.subject_repository as subject_repository
import repositories.learning_style_repository as learning_style_repository


def save(student):
    sql = "INSERT INTO students (first_name, last_name, subject_id, learning_style_id, comment) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [student.first_name, student.last_name,
              student.subject.id, student.learning_style.id, student.comment]
    results = run_sql(sql, values)
    student.id = results[0]['id']
    return student


def select_all():
    students = []

    sql = "SELECT * FROM students ORDER BY last_name"
    results = run_sql(sql)

    for row in results:
        subject = subject_repository.select(row['subject_id'])
        learning_style = learning_style_repository.select(
            row['learning_style_id'])
        student = Student(row['first_name'], row['last_name'], subject, learning_style, row['comment'], row['id'])
        students.append(student)
    return students


def select(id):
    student = None
    sql = "SELECT * FROM students WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
            subject = subject_repository.select(result['subject_id'])
            learning_style = learning_style_repository.select(
                result['learning_style_id'])
            student = Student(result['first_name'], result['last_name'], subject, learning_style, result['comment'], result['id'])
    return student


def delete_all():
    sql = "DELETE FROM students"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM students WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(student):
    sql = "UPDATE students SET (first_name, last_name, subject_id, learning_style_id, comment) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [student.first_name, student.last_name,
              student.subject.id, student.learning_style.id, student.comment, student.id]
    run_sql(sql, values)

# search for a student (pseudocode)
# define a function that will take in a search parameter. 
# assign an empty list to the variable students.
# sql query will search the students table for a match (using the LIKE operator).
# each student that matches the criteria will be added to the list (for loop).
# function will return the list of students that match the search parameter.

def search_for_student(student_name):
    students = []

    sql = "SELECT * FROM students WHERE first_name LIKE %s OR last_name LIKE %s"
    values = [f'%{student_name}%', f'%{student_name}%']
    results = run_sql(sql, values)

    for row in results:
        subject = subject_repository.select(row['subject_id'])
        learning_style = learning_style_repository.select(row['learning_style_id'])
        student = Student(row['first_name'], row['last_name'], subject, learning_style, row['comment'])
        students.append(student)
    return students

def subjects_for_student(student):
    subjects = []

    sql = "SELECT subjects.* FROM subjects INNER JOIN students ON students.subject_id = subjects.id WHERE students.id = %s"
    values = [student.id]
    results = run_sql(sql,values)

    for row in results:
        learning_style = learning_style_repository.select(row['learning_style_id'])
        subject = Subject(row['subject_name'], learning_style, row['id'])
        subjects.append(subject)
    return subjects
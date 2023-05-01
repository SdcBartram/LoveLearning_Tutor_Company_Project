from db.run_sql import run_sql

from models.lesson import Lesson
from models.subject import Subject
from models.student import Student
from models.learning_style import LearningStyle
from models.educator import Educator

import repositories.educator_repository as educator_repository
import repositories.subject_repository as subject_repository
import repositories.student_repository as student_repository
import repositories.learning_style_repository as learning_style_repository
import repositories.lesson_repository as lesson_repository


def save(lesson):
    sql = "INSERT INTO lessons (date, time, educator_id, student_id, subject_id, learning_style_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    if lesson.student:
        values = [lesson.date, lesson.time, lesson.educator.id,
                  lesson.student.id, lesson.subject.id, lesson.learning_style.id]
    else:
        values = [lesson.date, lesson.time, lesson.educator.id,
                  None, lesson.subject.id, lesson.learning_style.id]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson


def select_all():
    lessons = []

    sql = "SELECT * FROM lessons"
    results = run_sql(sql)

    for row in results:
        educator = educator_repository.select(row['educator_id'])
        student = student_repository.select(row['student_id'])
        subject = subject_repository.select(row['subject_id'])
        learning_style = learning_style_repository.select(
            row['learning_style_id'])
        lesson = Lesson(educator, student, subject, learning_style,
                        row['date'], row['time'], row['id'])
        lessons.append(lesson)
    return lessons

def select_all_upcoming_lessons():
    lessons = []

    sql = "SELECT * FROM lessons WHERE date >= CURDATE()"
    results = run_sql(sql)

    for row in results:
        educator = educator_repository.select(row['educator_id'])
        student = student_repository.select(row['student_id'])
        subject = subject_repository.select(row['subject_id'])
        learning_style = learning_style_repository.select(
            row['learning_style_id'])
        lesson = Lesson(educator, student, subject, learning_style,
                        row['date'], row['time'], row['id'])
        lessons.append(lesson)
    return lessons

def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = ['id']
    result = run_sql(sql, values)[0]

    if result is not None:
        for row in result:
            educator = educator_repository.select(row['educator_id'])
            student = student_repository.select(row['student_id'])
            subject = subject_repository.selct(row['subject_id'])
            learning_style = learning_style_repository.select(
                row['learning_style_id'])
        lesson = Lesson(educator, student, subject, learning_style,
                        row['date'], row['time'], row['id'])
    return lesson


def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM lessons WHERE id = %s"
    values = ['id']
    run_sql(sql, values)

# update lesson # add student to lesson


def update(lesson):
    if lesson.student is None:
        sql = "UPDATE lessons SET (date, time, educator_id, student_id, subject_id, learning_style_id) = (%s, %s, %s, NULL, %s, %s) WHERE id = %s"
        values = [lesson.date, lesson.time, lesson.educator.id,
                  lesson.subject.id, lesson.learning_style.id, lesson.id]
    else:
        sql = "UPDATE lessons SET (date, time, educator_id, student_id, subject_id, learning_style_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
        values = [lesson.date, lesson.time, lesson.educator.id, lesson.student.id,
                  lesson.subject.id, lesson.learning_style.id, lesson.id]
    run_sql(sql, values)


def students_for_lesson(student):
    classlist = []

    sql = "SELECT students.* FROM students INNER JOIN lessons ON lessons.student_id = students.id WHERE lessons.id = %s"
    values = [lesson.id]
    results = run_sql(sql, values)

    for row in results:
        subject = subject_repository.select(row['subject_id'])
        learning_style = learning_style_repository.select(
            row['learning_style_id'])
        student = Student(row['first_name'], row['last_name'],
                          subject, learning_style, row['comment'])
        classlist.append(student)
    return classlist

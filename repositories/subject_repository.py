from db.run_sql import run_sql

from models.subject import Subject
from models.learning_style import LearningStyle

import repositories.subject_repository as subject_repository
import repositories.learning_style_repository as learning_style_repository


def save(subject):
    sql = "INSERT INTO subjects (subject_name, learning_style_id) VALUES (%s, %s) RETURNING id"
    values = [subject.subject_name, subject.learning_style.id]
    results = run_sql(sql, values)
    subject.id = results[0]['id']
    return subject


def select_all():
    subjects = []

    sql = "SELECT * FROM subjects ORDER BY subject_name"
    results = run_sql(sql)

    for row in results:
        learning_style_id = row['learning_style_id']
        learning_style = learning_style_repository.select(learning_style_id)
        subject = Subject(row['subject_name'], learning_style, row['id'])
        subjects.append(subject)
    return subjects


def select(id):
    subject = None
    sql = "SELECT * FROM subjects WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        learning_style = learning_style_repository.select(
            result['learning_style_id'])
        subject = Subject(result['subject_name'], learning_style, result['id'])
    return subject


def delete_all():
    sql = "DELETE FROM subjects"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM subjects WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(subject):
    sql = "UPDATE subjects SET (subject_name, learning_style_id) = (%s, %s) WHERE id = %s"
    values = [subject.subject_name, subject.learning_style.id, subject.id]
    run_sql(sql, values)

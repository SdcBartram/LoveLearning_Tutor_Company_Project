from db.run_sql import run_sql

from models.educator import Educator
from models.subject import Subject
from models.learning_style import LearningStyle

import repositories.subject_repository as subject_repository
import repositories.learning_style_repository as learning_style_repository


def save(educator):
    sql = "INSERT INTO educators (first_name, last_name, subject_id, learning_style_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [educator.first_name, educator.last_name,
              educator.subject.id, educator.learning_style.id]
    results = run_sql(sql, values)
    educator.id = results[0]['id']
    return educator


def select_all():
    educators = []

    sql = "SELECT * FROM educators"
    results = run_sql(sql)

    for row in results:
        subject = subject_repository.select(row['subject_id'])
        learning_style = learning_style_repository.select(
            row['learning_style_id'])
        educator = Educator(
            row['first_name'], row['last_name'], subject, learning_style, row['id'])
        educators.append(educator)
    return educators


def select(id):
    educator = None
    sql = "SELECT * FROM educators WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        subject = subject_repository.select(result['subject_id'])
        learning_style = learning_style_repository.select(
            result['learning_style_id'])
        educator = Educator(
            result['first_name'], result['last_name'], subject, learning_style, result['id'])
    return educator


def delete_all():
    sql = "DELETE FROM educators"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM educators WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(educator):
    sql = "UPDATE educators SET (first_name, last_name, subject_id, learning_style_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [educator.first_name, educator.last_name, educator.subject.id, educator.learning_style.id, educator.id]
    run_sql(sql, values)


def subjects_for_educator(educator):
    subjects = []

    sql = "SELECT subjects.* FROM subjects INNER JOIN educators ON educators.subject_id = subjects.id WHERE educators.id = %s"
    values = [educator.id]
    results = run_sql(sql, values)

    for row in results:
        learning_style = learning_style_repository.select(
            row['learning_style_id'])
        subject = Subject(row['subject_name'], learning_style, row['id'])
        subjects.append(subject)
    return subjects

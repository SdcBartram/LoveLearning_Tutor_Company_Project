from db.run_sql import run_sql

from models.learning_style import LearningStyle

def save(educator):
    sql = "INSERT INTO educators "
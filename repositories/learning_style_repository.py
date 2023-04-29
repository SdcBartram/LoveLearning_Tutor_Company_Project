from db.run_sql import run_sql

from models.learning_style import LearningStyle

def save(learning_style):
    sql = "INSERT INTO learning_styles(learning_style) VALUES (%s) RETURNING id"
    values = [learning_style.learning_style]
    results = run_sql(sql, values)
    learning_style.id = results[0][id]
    return learning_style

def select_all():
    learning_styles = []

    sql = "SELECT * FROM learning_styles"
    results = run_sql(sql)

    for row in results:
        learning_style = LearningStyle(row['learning_style'], row['id'])
        learning_styles.append(learning_style)
    return learning_styles

def select(id):
    learning_style = None
    sql = "SELECT * FROM learning_styles WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        learning_style = LearningStyle(result['learning_style'], result['id'])
    return learning_style

def delete_all():
    sql = "DELETE FROM learning_styles"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM learning_styles WHERE id = %s"
    values = [id]
    run_sql(sql, values)


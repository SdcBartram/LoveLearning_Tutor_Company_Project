from flask import Flask, render_template

from controllers.subject_controller import subjects_blueprint
from controllers.student_controller import students_blueprint
from controllers.educator_controller import educators_blueprint
from controllers.lesson_controller import lessons_blueprint

app = Flask(__name__)

app.register_blueprint(subjects_blueprint)
app.register_blueprint(students_blueprint)
app.register_blueprint(educators_blueprint)
app.register_blueprint(lessons_blueprint)


@app.route('/')
def home():
    return render_template('index.jinja')


if __name__ == '__main__':
    app.run(debug=True)

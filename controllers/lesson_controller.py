from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.lesson import Lesson
from models.student_in_lesson import StudentInLesson
from models.learning_style import LearningStyle

import repositories.lesson_repository as lesson_repository
import repositories.subject_repository as subject_repository
import repositories.educator_repository as educator_repository
import repositories.learning_style_repository as learning_style_repository
import repositories.student_repository as student_repository
import repositories.student_in_lesson_repository as student_in_lesson_repository

lessons_blueprint = Blueprint("lessons", __name__)


@lessons_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.jinja", lessons=lessons)


@lessons_blueprint.route("/lessons/<id>")
def show(id):
    lesson = lesson_repository.select(id)
    return render_template("lessons/show.jinja", lesson=lesson)


@lessons_blueprint.route("/lessons/<id>/delete", methods=['POST'])
def delete_lesson(id):
    lesson_repository.delete(id)
    return redirect('/lessons')


@lessons_blueprint.route("/lessons/upcoming")
def upcoming_lessons():
    lessons = lesson_repository.select_all_upcoming_lessons()
    return render_template('/lessons/upcoming.jinja', lessons=lessons)


@lessons_blueprint.route("/lessons/new", methods=['GET'])
def new_lesson():
    educators = educator_repository.select_all()
    subjects = subject_repository.select_all()
    learning_styles = learning_style_repository.select_all()
    return render_template("lessons/new.jinja", all_educators=educators, all_subjects=subjects, all_learning_styles=learning_styles)


@lessons_blueprint.route("/lessons", methods=['POST'])
def create_lesson():
    print(request.form)
    date = request.form['date']
    time = request.form['time']
    educator = educator_repository.select(request.form['educator_id'])
    subject = subject_repository.select(request.form['subject_id'])
    learning_style = learning_style_repository.select(
        request.form['learning_style_id'])
    lesson = Lesson(date, time, educator, subject, learning_style)
    lesson_repository.save(lesson)
    return redirect('/lessons')


@lessons_blueprint.route("/lessons/<id>/edit", methods=['GET'])
def edit_lessons(id):
    subjects = subject_repository.select_all()
    learning_styles = learning_style_repository.select_all()
    educators = educator_repository.select_all()
    lesson = lesson_repository.select(id)
    return render_template("lessons/edit.jinja", lesson=lesson, all_educators=educators, all_subjects=subjects, all_learning_styles=learning_styles)


@lessons_blueprint.route("/lessons/<id>", methods=['POST'])
def update_lesson(id):
    date = request.form['date']
    time = request.form['time']
    subject = subject_repository.select(request.form['subject_id'])
    learning_style = learning_style_repository.select(
        request.form['learning_style_id'])
    educator = educator_repository.select(request.form['educator_id'])
    edited_lesson = Lesson(date, time, educator, subject, learning_style, id)
    lesson_repository.update(edited_lesson)
    return redirect('/lessons')


@lessons_blueprint.route("/lessons/<id>/students_in_lesson", methods=['GET'])
def student_in_lesson(id):
    lesson = lesson_repository.select(id)
    students_in_lesson = lesson_repository.students_for_lesson(lesson)
    return render_template("lessons/students_in_lesson.jinja", students_in_lesson=students_in_lesson, lesson=lesson)


@lessons_blueprint.route("/lesson/<id>/students", methods=['GET'])
def add_student_form(id):
    lesson = lesson_repository.select(id)
    students = student_repository.select_all()
    return render_template("lessons/add_student_to_lesson.jinja", all_students=students, lesson=lesson)


@lessons_blueprint.route("/add_student_to_lesson/<id>", methods=['POST'])
def add_student_to_lesson(id):
    lesson = lesson_repository.select(id)
    student = student_repository.select(request.form['student_id'])
    if student.id in [student.id for student in lesson_repository.students_for_lesson(lesson)]:
        return render_template("lessons/student_already_in_lesson.jinja", student=student, lesson=lesson)
    if len(lesson_repository.students_for_lesson(lesson)) >= 3:
        return render_template("lessons/too_many_students.jinja", lesson=lesson)
    if student.learning_style.id != lesson.learning_style.id:
        print(student.learning_style.id)
        print(lesson.learning_style.id)
        return render_template("lessons/learning_style_does_not_match.jinja", student=student, lesson=lesson)
    print("HERE!!!", lesson.id, lesson.learning_style.id)
    new_student_in_lesson = StudentInLesson(student, lesson, id)
    student_in_lesson_repository.save(
        new_student_in_lesson.student.id, new_student_in_lesson.lesson.id)
    return redirect(f"/lessons/{id}/students_in_lesson")


# Function to display all students in a lesson
# Select the lesson with the given id
# Render the students_in_lesson template with the list of students and the lesson
# Function to add a student to a lesson
# Select the lesson with the given id
# Select the student with the id provided in the form
# conditional statement to check the length of list of students has not reached the max
# conditional statement to check that learning_styles match
# Create a new StudentInLesson object and save it to the database
# increase count to list of students
# Redirect to the page displaying the students in the lesson


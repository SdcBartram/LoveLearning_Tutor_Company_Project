from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.lesson import Lesson

import repositories.lesson_repository as lesson_repository
import repositories.subject_repository as subject_repository
import repositories.educator_repository as educator_repository
import repositories.learning_style_repository as learning_style_repository

lessons_blueprint = Blueprint("lessons", __name__)


@lessons_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.jinja", lessons=lessons)


@lessons_blueprint.route("/lessons/<id>")
def show(id):
    lesson = lesson_repository.select(id)
    return render_template("lessons/show.jinja", lesson=lesson)


@lessons_blueprint.route("/lessons/<id>/edit", methods=['GET'])
def edit_lessons(id):
    lesson = lesson_repository.select(id)
    return render_template("lessons/edit.jinja", lesson=lesson)


@lessons_blueprint.route("/lessons/<id>/delete", methods=['POST'])
def delete_lesson(id):
    lesson_repository.delete(id)
    return redirect('/lessons')


@lessons_blueprint.route("/lessons/upcoming")
def upcoming_lessons():
    lessons = lesson_repository.select_all_upcoming_lessons()
    return render_template('/lessons/upcoming.jinja', lessons=lessons)


@lessons_blueprint.route("/lessons/<id>/students_in_lesson")
def student_in_lesson(id):
    lesson = lesson_repository.select(id)
    students = lesson_repository.students_for_lesson(lesson)
    return render_template("lessons/students_in_lesson.jinja", students=students)

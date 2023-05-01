from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.student import Student

import repositories.student_repository as student_repository
import repositories.learning_style_repository as learning_style_repository
import repositories.subject_repository as subject_repository

students_blueprint = Blueprint("students", __name__)


@students_blueprint.route("/students")
def students():
    students = student_repository.select_all()
    return render_template("students/index.jinja", students=students)

@students_blueprint.route("/students/<id>")
def show(id):
    student = student_repository.select(id)
    return render_template("students/show.jinja", student=student)

@students_blueprint.route("/students/<id>/edit", methods=['GET'])
def edit_students(id):
    student = student_repository.select(id)
    return render_template("students/edit.jinja", student=student)

@students_blueprint.route("/students/<id>/delete", methods=['POST'])
def delete_educator(id):
    student_repository.delete(id)
    return redirect('/students')

# student search
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.student import Student

import repositories.student_repository as student_repository

students_blueprint = Blueprint("students", __name__)


@students_blueprint.route("/students")
def students():
    students = student_repository.select_all()
    return render_template("students/index.jinja", students=students)

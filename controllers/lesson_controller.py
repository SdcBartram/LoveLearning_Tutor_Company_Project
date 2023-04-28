from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.lesson import Lesson

import repositories.lesson_repository as lesson_repository

lessons_blueprint = Blueprint("lessons", __name__)


@lessons_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.jinja", lessons=lessons)

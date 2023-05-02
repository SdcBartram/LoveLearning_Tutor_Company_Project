from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.student_in_lesson import StudentInLesson
from models.lesson import Lesson
from models.student import Student

import repositories.lesson_repository as lesson_repository
import repositories.student_repository as student_repository
import repositories.student_in_lesson_repository as student_in_lesson_repository

student_in_lesson_blueprint = Blueprint("student_in_lesson", __name__)


@student_in_lesson_blueprint.route("/add_student_to_lesson/<id>", methods=['POST'])
def add_student_to_lesson(id):
    lesson = lesson_repository.select(id)
    student = student_repository.select(request.form['student_id'])
    new_student_in_lesson = StudentInLesson(student, lesson, id)
    student_in_lesson_repository.save(new_student_in_lesson)
    return redirect("/lessons/{}/students_in_lesson".format(id))

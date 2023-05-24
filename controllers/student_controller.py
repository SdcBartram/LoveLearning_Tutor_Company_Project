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



@students_blueprint.route("/students/<id>/delete", methods=['POST'])
def delete_educator(id):
    student_repository.delete(id)
    return redirect('/students')


@students_blueprint.route("/students/new", methods=['GET'])
def new_student():
    subjects = subject_repository.select_all()
    learning_styles = learning_style_repository.select_all()
    return render_template("students/new.jinja", all_subjects=subjects, all_learning_styles=learning_styles)


@students_blueprint.route("/students", methods=['POST'])
def create_student():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    subject = subject_repository.select(request.form['subject_id'])
    learning_style = learning_style_repository.select(
        request.form['learning_style_id'])
    comment = request.form['comment']
    student = Student(first_name, last_name, subject, learning_style, comment)
    student_repository.save(student)
    return redirect('/students')

@students_blueprint.route("/students/<id>/edit", methods=['GET'])
def edit_students(id):
    subjects = subject_repository.select_all()
    learning_styles = learning_style_repository.select_all()
    student = student_repository.select(id)
    return render_template("students/edit.jinja", student=student, all_subjects=subjects, all_learning_styles=learning_styles)


@students_blueprint.route("/students/<id>", methods=['POST'])
def update_student(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    subject = subject_repository.select(request.form['subject_id'])
    learning_style = learning_style_repository.select(
        request.form['learning_style_id'])
    comment = request.form['comment']
    edited_student = Student(first_name, last_name, subject, learning_style, comment, id)
    student_repository.update(edited_student)
    return redirect('/students')


# # student search
# @students_blueprint.route("/students/<id>/search", methods=['GET'])
# def find_student(id):
#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     student = Student(first_name, last_name, id)
#     student_repository.search_for_student(student)
#     return redirect('/students/{}'.format(id))



from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.subject import Subject

import repositories.subject_repository as subject_repository
import repositories.learning_style_repository as learning_style_repository


subjects_blueprint = Blueprint("subjects", __name__)


@subjects_blueprint.route("/subjects")
def subjects():
    subjects = subject_repository.select_all()
    return render_template("subjects/index.jinja", subjects=subjects)

@subjects_blueprint.route("/subjects/<id>")
def show(id):
    subject = subject_repository.select(id)
    return render_template("subjects/show.jinja", subject=subject)

@subjects_blueprint.route("/subjects/<id>/delete", methods=['POST'])
def delete_subject(id):
    subject_repository.delete(id)
    return redirect('/subjects')
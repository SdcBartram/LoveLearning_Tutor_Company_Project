from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.subject import Subject

import repositories.subject_repository as subject_repository


subjects_blueprint = Blueprint("subjects", __name__)


@subjects_blueprint.route("/subjects")
def subjects():
    subjects = subject_repository.select_all()
    return render_template("subjects/index.jinja", subjects=subjects)

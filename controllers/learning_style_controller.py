from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.learning_style import LearningStyle

import repositories.learning_style_repository as learning_style_repository

learning_styles_blueprint = Blueprint("learning_style", __name__)


@learning_styles_blueprint.route("/learning_styles")
def learning_styles():
    learning_styles = learning_style_repository.select_all()
    return render_template("learning_style/index.jinja", learning_styles=learning_styles)

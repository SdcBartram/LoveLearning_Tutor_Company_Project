from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.educator_repository as educator_repository
import repositories.subject_repository as subject_repository
import repositories.learning_style_repository as learning_style_repository

educators_blueprint = Blueprint("educators", __name__)


@educators_blueprint.route("/educators")
def educators():
    educators = educator_repository.select_all()
    return render_template("educators/index.jinja", educators=educators)

@educators_blueprint.route("/educators/<id>")
def show(id):
    educator = educator_repository.select(id)
    subject = subject_repository.select(id)
    return render_template("educators/show.jinja", educator=educator, subject=subject)

@educators_blueprint.route("/educators/<id>/edit", methods=['GET'])
def edit_educators(id):
    educator = educator_repository.select(id)
    return render_template("educators/edit.jinja", educator=educator)

@educators_blueprint.route("/educators/<id>/delete", methods=['POST'])
def delete_educator(id):
    educator_repository.delete(id)
    return redirect('/educators')

# @educators_blueprint.route("/educators/<id>", methods=['POST'])
# def update_educators(id):
#     educator = educator_repository.select(id)
#     educator.first_name = request.form['first_name']
#     educator.last_name = request.form['last_name']
#     subject_id = request.form['subject_id']
#     subject = subject_repository.select(subject_id)
#     educator.subject = subject
#     learning_style_id = request.form['learning_style_id']
#     learning_style = learning_style_repository.select(learning_style_id)
#     educator.learning_style = learning_style
#     educator_repository.update(educator)
#     return redirect('/educators')

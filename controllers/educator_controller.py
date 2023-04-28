from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.educator_repository as educator_repository

educators_blueprint = Blueprint("educators", __name__)


@educators_blueprint.route("/educators")
def educators():
    educators = educator_repository.select_all()
    return render_template("educators/index.jinja", educators=educators)

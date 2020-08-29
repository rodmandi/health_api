from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from core.controllers import health_controller

health_blueprint = Blueprint('health_routes', __name__, url_prefix='/health_services')


@health_blueprint.route('/get_true_value', methods=['POST'])
def process_mail():
    return health_controller.get_true_value(request.json)


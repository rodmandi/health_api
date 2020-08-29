from gevent import monkey
monkey.patch_all()


import flask
from routing.routing import health_blueprint
from core.helpers.DefaultLogger import DefaultLogger

logger = DefaultLogger.get_logger(__name__)
DefaultLogger.set_root_logger_basic_config()


app = flask.Flask('__main__')
app.register_blueprint(health_blueprint)


@app.before_first_request
def initialize():
    logger.info("Initializing API - Receiving First request")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000, debug=True)



"""
main run for flask.

Date of birth: 07-09-2021
Sire to: BaradDur

"""

import flask
import flask_restful

"get workers"
from make_celery import make_celery

"get views"
from view.views import add_views

app = flask.Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

"add workers"
celery = make_celery(app)
app.celery = celery

"register blueprints"
with app.app_context():
    add_views()

if __name__ == '__main__':
    app.run()
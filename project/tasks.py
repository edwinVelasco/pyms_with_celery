from flask import Blueprint, current_app
from celery import Celery

from manage import app as App


def make_celery(app):
    cel = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    cel.conf.update(app.config)

    class ContextTask(cel.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    cel.Task = ContextTask
    return cel


celery = make_celery(App)

@celery.task(name='add_together')
def add_together(a, b):
    with App.app_context():
        print(a+b)

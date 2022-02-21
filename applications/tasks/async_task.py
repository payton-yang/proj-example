from applications.test_web.service import TestWebService
from .celery_instance import app


@app.task(name='test_sub')
def sub(x, y):
    print(f'{x} - {y} = {x - y}')


@app.task(name='test_task')
def test_task(name):
    TestWebService(name).run()

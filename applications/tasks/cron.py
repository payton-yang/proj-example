from celery import shared_task


@shared_task(name='test_cron')
def test_cron(x, y):
    print(f'test: {x} + {y} = {x + y}')

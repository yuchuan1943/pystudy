from celery import Celery
from celery.schedules import crontab

broker = 'amqp://guest@localhost//'
app = Celery('test', broker=broker)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    print(sender)
    # Calls test('hello') every 3 seconds.
    sender.add_periodic_task(3, test.s('hello'), name='add every 3')

    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )


@app.task
def test(arg):
    print(arg)

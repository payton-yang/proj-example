import time

from applications.test_web.models import TestWeb


class TestWebService:
    def __init__(self, name):
        self.name = name

    def run(self):
        time.sleep(2)
        TestWeb(name=self.name).save()

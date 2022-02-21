from rest_framework.views import APIView
from rest_framework.response import Response

from applications.tasks.async_task import test_task
from applications.utils.try_catch import CatchException


class TestView(APIView):
    @CatchException
    def get(self, request):
        # x = 1 / 0
        return Response(data={'code': 200, 'msg': 'success!!!'})

    def post(self, request):
        data = request.data
        name = data.get('name', None)
        if not name:
            return Response(data={'code': 400, 'msg': 'name is required!!!'})
        test_task.delay(name)
        return Response(data={'code': 200, 'msg': 'tasks success!!!'})

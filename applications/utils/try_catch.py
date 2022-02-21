import logging
import traceback
from functools import wraps

from rest_framework.response import Response

from applications.utils.obj_response import ObjectResp
from applications.utils.response_code import HTTP, ERR_MAP_HTTP

logger = logging.getLogger('errMsg')


class CatchException:
    def __init__(self, func):
        wraps(func)(self)

    def __call__(self, request, *args, **kwargs):

        try:
            return self.__wrapped__(self, request, *args, **kwargs)
        except Exception as e:
            logger.error(f'{traceback.format_exc()}')

            resp = Response(ObjectResp.response(
                code=HTTP.HTTP_500_INTERNAL_SERVER_ERROR,
                message=ERR_MAP_HTTP[HTTP.HTTP_500_INTERNAL_SERVER_ERROR]
            ))
        return resp

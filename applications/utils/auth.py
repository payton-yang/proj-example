from django.conf import settings
from rest_framework.request import Request
from django.http import JsonResponse, HttpRequest

from applications.utils.response_code import HTTP
from applications.utils.obj_response import ObjectResp


def auth_token(func):
    def wrapper(*args, **kwargs):
        for x in args:
            if isinstance(x, HttpRequest) or isinstance(x, Request):
                request = x
        key = 'HTTP_X_AUTH_TOKEN'

        if key not in request.META:
            return JsonResponse(ObjectResp.response(code=HTTP.HTTP_401_UNAUTHORIZED_ERROR,
                                                    message='Must provide X-Auth-Token header to this endpoint'))

        x_store_hash_key = 'HTTP_X_STOREHASH'
        if x_store_hash_key not in request.META:
            return JsonResponse(ObjectResp.response(code=HTTP.HTTP_401_UNAUTHORIZED_ERROR,
                                                    message='Must provide X-Auth-Token header to this endpoint'))

        token = request.META[key]
        store_hash = request.META[x_store_hash_key]
        stores = settings.HTTP_AUTH_TOKEN

        source_token = str(stores.get(store_hash, None))
        if str(token) != str(source_token):
            return JsonResponse(ObjectResp.response(code=HTTP.HTTP_403_FORBIDDEN_ERROR, message='Invalid token'))

        request.META['user_information'] = {
            'store_hash': store_hash,
        }

        return func(*args, **kwargs)

    return wrapper

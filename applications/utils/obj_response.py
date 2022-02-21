from applications.utils.response_code import ERR_MAP, RET


class ObjectResp:

    @staticmethod
    def response(code=None, message=None, **response):
        if code is None:
            code = RET.HTTP_200_OK
        if message is None:
            message = ERR_MAP[RET.HTTP_200_OK]
        result = {
            'code': code,
            'message': message,
            'data': response
        }
        return result

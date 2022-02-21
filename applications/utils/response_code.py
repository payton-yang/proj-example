from django.utils.translation import gettext_lazy as _


class HTTP:
    HTTP_200_SUCCESS = 200
    HTTP_400_BAD_REQUEST_ERROR = 400
    HTTP_401_UNAUTHORIZED_ERROR = 401
    HTTP_403_FORBIDDEN_ERROR = 403
    HTTP_422_PARAMETER_ERROR = 422
    HTTP_500_INTERNAL_SERVER_ERROR = 500
    HTTP_404_NOT_FOUND_ERROR = 404


ERR_MAP_HTTP = {
    200: _("Success"),
    400: _("Bad Requests Error"),
    401: _("Unauthorized Error"),
    422: _("Parameter Error"),
    403: _("Forbidden Error"),
    500: _("Internal Server Error"),
    404: _("Not Found Error")
}


class RET:
    HTTP_200_OK = 200
    HTTP_500_INTER_SERVER_ERROR = 500
    HTTP_PARAMETER_TYPE_ERROR = 10010
    HTTP_PARAMETER_NOT_FOUND = 10011
    HTTP_PARAMETER_VALUE_ERROR = 10012
    HTTP_PARAMETER_NOT_ALLOW_NULL = 10013
    HTTP_DATA_MODEL_ERROR = 10014
    HTTP_USER_DOES_NOT_EXIST = 10015
    HTTP_AUTHENTICATION_ERROR = 10016
    HTTP_COMPANY_ILLEGAL = 10017
    HTTP_SERVER_BUSY = 10018
    HTTP_ROLE_ERROR = 10019
    HTTP_PERMISSION_DENIED = 10020
    HTTP_BACKEND_USER_NOT_FOUND = 10021
    HTTP_BACKEND_ROLE_NOT_FOUND = 10022
    HTTP_REQUEST_DENIED = 10023


ERR_MAP = {
    200: _("SUCCESS"),
    500: _("INTERVAL SERVER ERROR"),
    10010: _("PARAMETER TYPE ERROR"),
    10011: _("PARAMETER NOT FOUND"),
    10012: _("PARAMETER VALUE ERROR"),
    10013: _("PARAMETER VALUE NOT ALLOW NULL"),
    10014: _("DATA MODEL ERROR"),
    10015: _("USER DOES NOT EXIST"),
    10016: _("INVALID TOKEN HEADER, TOKEN STRING SHOULD NOT CONTAIN INVALID CHARACTERS."),
    10017: _("COMPANY ILLEGAL: CAN NOT FOUND"),
    10018: _("SERVER BUSY, PLEASE TRY AGAIN LATER"),
    10019: _("USER ROLE ERROR"),
    10020: _("PERMISSION DENIED"),
    10021: _("BACKEND USER NOT FOUND"),
    10022: _("BACKEND ROLE NOT FOUND"),
    10023: _("ILLOGICAL OPERATION. REQUEST DENIED")
}


class SerializerMsg:

    def __init__(self, field):
        self.field = str(field).capitalize()

    @property
    def required_msg(self):
        return f"{self.field} is required."

    @property
    def null_msg(self):
        return f"{self.field} not allow none."

    @property
    def blank_msg(self):
        return f"{self.field} not allow blank."

    @property
    def invalid_msg(self):
        return f"Invalid {self.field}."

    def max_length_msg(self, max_length):
        return f"{self.field} cannot exceed {max_length} characters"

    @property
    def empty_msg(self):
        return f"{self.field} not allow empty."

    @property
    def choice_msg(self):
        return f"{self.field} is not valid choice."

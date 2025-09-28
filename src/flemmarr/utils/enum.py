from enum import Enum


class ApiType(Enum):
    DELETE = 0
    GET = 1
    GET_SCHEMA = 2
    POST = 3
    PUT = 4


class ApiPrefix(str, Enum):
    DELETE = "delete_api_v3"
    GET = "get_api_v3"
    GET_SCHEMA = "get_api_v3"
    POST = "post_api_v3"
    PUT = "put_api_v3"


class MergeKey(Enum):
    DEFAULT = 0
    NONE = 1
    NAME = 2
    TITLE = 3
    IMPLEMENTATION = 4


class Strategy(Enum):
    DEFAULT = 0
    SINGLE = 1
    BULK = 2

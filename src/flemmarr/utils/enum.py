from enum import Enum, StrEnum, auto


class MergeKey(StrEnum):
    NONE = auto()
    SINGLE_ITEM = auto()
    NAME = auto()
    TITLE = auto()
    IMPLEMENTATION = auto()


class Strategy(Enum):
    NONE = auto()
    SINGLE = auto()
    BULK = auto()

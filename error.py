from abc import ABC

class ErrorObject(ABC):
    pass

class Okay(ErrorObject):
    def __init__(self) -> None:
        super().__init__()

class Error(ErrorObject):
    def __init__(self, msg: str) -> None:
        super().__init__()
        self.msg = msg

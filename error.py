class ErrorObject:
    def __init__(self, msg: str) -> None:
        self.msg = msg

class Okay(ErrorObject):
    def __init__(self) -> None:
        super().__init__('')

class Error(ErrorObject):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

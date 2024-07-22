from abc import ABC, abstractmethod

'''
    Lists different forms of counters
'''
class Counter(ABC):
    @abstractmethod
    def countdown(self, dt: float) -> bool:
        'returns a bool indicating its time has run out'
        pass

class SecondsCounter(Counter):
    def __init__(self, life: float) -> None:
        super().__init__()
        self.life = life
        self.max = life

    def countdown(self, dt: float) -> bool:
        self.life -= dt
        return self.life <= 0

class FrameCounter(Counter):
    def __init__(self, frames: int) -> None:
        super().__init__()
        self.frames = frames

    def countdown(self, dt: float) -> bool:
        self.frames -= 1
        return self.frames <= 0

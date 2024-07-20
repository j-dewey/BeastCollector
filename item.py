from abc import ABC, abstractmethod
from enum import Enum
from typing_extensions import Any

class ItemEffectType(Enum):
    SPAWN_PARTY_MEMBER = 0

class ItemEffect:
    def __init__(self, type: ItemEffectType, data: Any) -> None:
        self.type = type
        self.data = data

class Item(ABC):
    @abstractmethod
    def get_effect(self) -> ItemEffect: pass

class

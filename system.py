from abc import ABC, abstractmethod


class System(ABC):
    """Abstract class for processing Entity instances."""
    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        """The update method that is called every tick.

        :return: None
        """
        pass

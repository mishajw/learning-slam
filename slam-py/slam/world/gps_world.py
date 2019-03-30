from . import World

from typing import List
import numpy as np


class GpsWorld(World):
    def __init__(self):
        self.location = np.zeros(2)

    def step(self):
        self.location += [1, 0]

    def get_location(self) -> np.array:
        return self.location

    def get_map(self) -> List[np.array]:
        return []

    def get_motion(self) -> np.array:
        return np.array([1, 0])

    def get_observation(self) -> np.array:
        return self.location

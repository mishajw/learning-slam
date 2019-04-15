from typing import List
import numpy as np


class World:
    def step(self):
        raise NotImplementedError()

    def get_location(self) -> np.array:
        raise NotImplementedError()

    def get_map(self) -> List[np.array]:
        raise NotImplementedError()

    def get_motion(self) -> np.array:
        raise NotImplementedError()

    def get_observation(self) -> np.array:
        raise NotImplementedError()

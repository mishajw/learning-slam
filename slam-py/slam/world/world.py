from typing import List
import numpy as np

class World:
    def step(self):
        raise NotImplemented()

    def get_location(self) -> np.array:
        raise NotImplemented()

    def get_map(self) -> List[np.array]:
        raise NotImplemented()

    def get_motion(self) -> np.array:
        raise NotImplemented()

    def get_observation(self) -> np.array:
        raise NotImplemented()

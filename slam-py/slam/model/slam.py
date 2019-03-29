from typing import List
import numpy as np

class Slam:
    """Model that performs Simultaneous Localisation and Mapping (SLAM)"""

    def step(self, motion: np.array, observations: np.array):
        """Update predictions based on new observations and motion"""
        raise NotImplemented()

    def get_map(self) -> List[np.array]:
        """Get the predicted map"""
        raise NotImplemented()

    def get_location(self) -> np.array:
        """Get the predicted location"""
        raise NotImplemented()

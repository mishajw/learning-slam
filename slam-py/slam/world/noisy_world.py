from . import World

from typing import List
import numpy as np

class NoisyWorld(World):
    def __init__(
            self, world: World, motion_noise: float, observation_noise: float):
        self.world = world
        self.motion_noise = motion_noise
        self.observation_noise = observation_noise

    def step(self):
        self.world.step()

    def get_location(self) -> np.array:
        return self.world.get_location()

    def get_map(self) -> List[np.array]:
        return self.world.get_map()

    def get_motion(self) -> np.array:
        motion = self.world.get_motion()
        return motion + np.random.uniform(
            low=-self.motion_noise,
            high=self.motion_noise,
            size=motion.shape)

    def get_observation(self) -> np.array:
        observation = self.world.get_observation()
        return observation + np.random.uniform(
            low=-self.observation_noise,
            high=self.observation_noise,
            size=observation.shape)

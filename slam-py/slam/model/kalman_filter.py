from . import Slam

from numpy.linalg import inv
from typing import List
import numpy as np

class KalmanFilter(Slam):
    def __init__(
            self,
            state_transition: np.array,
            motion_transition: np.array,
            observation_transition: np.array,
            motion_noise: np.array,
            observation_noise: np.array):
        self.num_states = state_transition.shape[0]
        self.num_motions = motion_transition.shape[1]
        self.num_observations = observation_transition.shape[1]
        assert state_transition.shape == (self.num_states, self.num_states)
        assert motion_transition.shape == (self.num_states, self.num_motions)
        assert observation_transition.shape == \
            (self.num_states, self.num_observations)
        assert motion_noise.shape == (self.num_states, self.num_states)
        assert observation_noise.shape == (self.num_states, self.num_states)

        self.state_transition = state_transition
        self.motion_transition = motion_transition
        self.observation_transition = observation_transition
        self.motion_noise = motion_noise
        self.observation_noise = observation_noise
        self.state_mean = np.zeros(self.num_states)
        self.state_variance = np.eye(self.num_states)

    @classmethod
    def create_2d(cls):
        return KalmanFilter(
            np.eye(2), np.eye(2), np.eye(2), np.eye(2), np.eye(2))

    def step(self, motion: np.array, observations: np.array):
        assert motion.shape == (self.num_motions,)
        assert observations.shape == (self.num_observations,)

        state_mean = self.state_transition.dot(self.state_mean) + \
            self.motion_transition.dot(motion)
        state_variance = self.state_transition \
            .dot(self.state_variance) \
            .dot(self.state_transition.T) + self.motion_noise

        kalman_gain = state_variance.dot(self.observation_transition.T).dot(
            inv(self.observation_transition \
                .dot(state_variance) \
                .dot(self.observation_transition.T) + self.observation_noise)
        )

        self.state_mean = state_mean + kalman_gain.dot(
            observations - self.observation_transition.dot(state_mean)
        )
        self.state_variance = (
            np.eye(self.num_states) - kalman_gain.dot(self.observation_transition)
        ).dot(state_variance)

    def get_location(self) -> List[np.array]:
        return self.state_mean

    def get_location_variance(self) -> np.array:
        return self.state_variance

    def get_map(self) -> List[np.array]:
        return []

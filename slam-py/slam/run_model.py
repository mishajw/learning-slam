from .model import Slam
from .world import World

from itertools import count
from typing import Iterator


def run_model(model: Slam, world: World) -> Iterator[int]:
    for i in count():
        motion = world.get_motion()
        observation = world.get_observation()
        model.step(motion, observation)
        world.step()
        yield i

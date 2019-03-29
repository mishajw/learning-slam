from .model import Slam
from .world import World

from typing import Iterator
import pygame

WIDTH = 800
HEIGHT = 600

MODEL_LOCATION_COLOR = (255, 0, 0)
WORLD_LOCATION_COLOR = (0, 255, 0)
MODEL_LANDMARK_COLOR = (255, 0, 255)
WORLD_LANDMARK_COLOR = (0, 255, 255)

LOCATION_RADIUS = 10
LANDMARK_RADIOS = 5

def draw(model: Slam, world: World, step_iter: Iterator[int]):
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("SLAM")
    clock = pygame.time.Clock()

    min_location, max_location = -100, 100

    def scale_location(location):
        nonlocal min_location, max_location
        min_location = min(min_location, location[0], location[1])
        max_location = max(max_location, location[0], location[1])
        scale = (max_location - min_location) / min(WIDTH, HEIGHT)
        return \
            int((location[0] - min_location) / scale), \
            int((location[1] - min_location) / scale)

    for step_index in step_iter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        model_location = model.get_location()
        model_map = model.get_map()
        world_location = world.get_location()
        world_map = world.get_map()
        pygame.draw.circle(
            screen,
            MODEL_LOCATION_COLOR,
            scale_location(model_location),
            LOCATION_RADIUS,
            LOCATION_RADIUS)
        pygame.draw.circle(
            screen,
            WORLD_LOCATION_COLOR,
            scale_location(world_location),
            LOCATION_RADIUS,
            LOCATION_RADIUS)
        # TODO: Draw landmarks

        pygame.display.flip()
        clock.tick(5)

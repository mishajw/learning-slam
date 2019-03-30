from .model import Slam
from .world import World

from math import pi
from typing import Iterator
import numpy as np
import pygame

WIDTH = 800
HEIGHT = 600

MODEL_LOCATION_COLOR = (255, 0, 0)
WORLD_LOCATION_COLOR = (0, 255, 0)
MODEL_LANDMARK_COLOR = (255, 0, 255)
WORLD_LANDMARK_COLOR = (0, 255, 255)

LOCATION_RADIUS = 4
LANDMARK_RADIUS = 2


def draw(model: Slam, world: World, step_iter: Iterator[int]):
    pygame.init()
    surface = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("SLAM")
    clock = pygame.time.Clock()

    min_location, max_location = -10, 10

    def scale_location(location):
        nonlocal min_location, max_location
        min_location = min(min_location, location[0], location[1])
        max_location = max(max_location, location[0], location[1])
        scale = min(WIDTH, HEIGHT) / (max_location - min_location)
        return (
            int((location[0] - min_location) * scale),
            int((location[1] - min_location) * scale),
        )

    def scale_size(size: float):
        return size * min(WIDTH, HEIGHT) / (max_location - min_location)

    def draw_location(location: np.array, color):
        nonlocal surface
        pygame.draw.circle(
            surface, color, scale_location(location), LOCATION_RADIUS, LOCATION_RADIUS
        )

    def draw_variance(location: np.array, variance: np.array, color):
        nonlocal surface
        eig_values, eig_vectors = np.linalg.eig(variance)
        eig_values = np.sqrt(eig_values)
        width = scale_size(eig_values[0])
        height = scale_size(eig_values[1])
        angle = np.arccos(eig_vectors[0, 0])
        print(width, height, angle)

        rot_surface = pygame.Surface((width, height))
        pygame.draw.ellipse(rot_surface, color, [0, 0, width, height], 1)
        rot_surface = pygame.transform.rotate(rot_surface, np.rad2deg(angle))
        x, y = scale_location(location)
        surface.blit(rot_surface, (x - width // 2, y - height // 2))

    for step_index in step_iter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        surface.fill((0, 0, 0))

        model_location = model.get_location()
        model_location_variance = model.get_location_variance()
        model_map = model.get_map()
        world_location = world.get_location()
        world_map = world.get_map()
        draw_variance(model_location, model_location_variance, MODEL_LOCATION_COLOR)
        draw_location(model_location, MODEL_LOCATION_COLOR)
        draw_location(world_location, WORLD_LOCATION_COLOR)
        # TODO: Draw landmarks

        pygame.display.flip()
        clock.tick(5)

from slam.model import KalmanFilter
from slam.world import GpsWorld, NoisyWorld
from slam import run_model, draw

import numpy as np


def main():
    model = KalmanFilter.create_2d()
    world = NoisyWorld(GpsWorld(), 0.5, 0.5)
    run = run_model(model, world)
    draw(model, world, run)


if __name__ == "__main__":
    np.set_printoptions(precision=3, suppress=True)
    main()

from slam.model import KalmanFilter
from slam.world import GpsWorld, NoisyWorld
from slam import run_model

import numpy as np

def main():
    model = KalmanFilter.create_2d()
    world = NoisyWorld(GpsWorld(), 0.5, 0.5)
    run = run_model(model, world)
    for step_index in run:
        print(step_index)
        print(model.get_location())

if __name__ == "__main__":
    np.set_printoptions(precision=3, suppress=True)
    main()

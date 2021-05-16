import json

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import itertools
from Greenhouse import Greenhouse
from Plant import Plant
from logger import Logger, Event
from visualization import plot_data, plot_greenhouse
import argparse
import time

##############################
# PRESETS AND GLOBAL VARIABLES
##############################
FRAMES = 50
HEIGHT = 50
WIDTH = 50
SCALE = 1
DAILY_WATER = 1

# Each plant has a name to be used in command argument (--setup)
PLANT_PARAMS = {
    "single-plant": {
        "seed": 12345,
        "plants": lambda: [Plant(20, 20, color='g')]
    },
    "control-and-3": {
        "seed": 38572912,
        "plants": lambda: [Plant(20, 20, color='g'), Plant(23, 23, color='b'), Plant(22, 22, color='k'),
                           Plant(40, 40, color='c')]
    },
    "greedy-plant-limited": {
        "seed": 6937103,
        "plants": lambda: [Plant(30, 30, color='b'), Plant(31, 31, color='r', l_effect=2, growth_time=15)]
    },
    "greedy-plant-fulfilled": {
        "seed": 6937103,
        "daily-water": 2,
        "plants": lambda: [Plant(30, 30, color='b'), Plant(31, 31, color='r', l_effect=2, growth_time=9)]
    },
    "faster-plant": {
        "seed": 76721,
        "plants": lambda: [Plant(25, 25, color='g'), Plant(26, 26, color='tab:orange', w_effect=0.15, growth_time=15),
                           Plant(25, 29, color='c')]
    },
    "random": {
        "seed": None,
        "plants": lambda: _get_random_plants()
    }
}

WATERING_SCHEDULE = {
    "sequential": {
        "policy": lambda: _make_sequential_irrigator(10, 4, 30)
    },
    "downhill": {
        "policy": lambda: _make_downhill_irrigator(10, 1, 20)
    },
    "row": {
        "policy": lambda: _make_row_irrigator(10, 1, 30)
    },
    "random": {
        "policy": lambda: _make_random_irrigator(4)
    }
}


def _make_sequential_irrigator(grid_step, amount, shift):
    def get_sequential_irrigation(timestep):
        # print("old timestep", timestep)
        row_max = WIDTH // grid_step
        col_max = HEIGHT // grid_step
        timestep = (timestep + shift) % (row_max * col_max)
        # print("new timestep", timestep)
        row = timestep // col_max
        col = timestep % col_max
        print("row:", row, "col", col)
        i, j = row * grid_step + grid_step // 2, col * grid_step + grid_step // 2
        # i = (1 * 10) + (10 // 2), j = (0*10)+ (10 //2)
        # i = 15, j = 5
        print("i:", i, "j", j)
        irrigations = [0] * (HEIGHT * WIDTH)
        irrigations[i * HEIGHT + j] = amount
        return irrigations

    return get_sequential_irrigation


def _make_downhill_irrigator(grid_step, amount, shift):
    def get_downhill_irrigation(timestep):
        # print("old timestep", timestep)
        row_max = WIDTH // grid_step
        col_max = HEIGHT // grid_step
        timestep = (timestep + shift) % (col_max)
        print("new timestep", timestep)
        row = timestep // col_max
        col = timestep % col_max
        print("row:", row, "col", col)
        i, j = row * grid_step + grid_step // 2, col * grid_step + grid_step // 2
        print("i:", row, "j", col)
        irrigations = [0] * (HEIGHT * WIDTH)
        irrigations[i * HEIGHT + j] = (amount * timestep) + 0.5
        irrigations[(i + grid_step) * HEIGHT + j] = (amount * timestep) + 0.5
        irrigations[(i + (grid_step * 2)) * HEIGHT + j] = (amount * timestep) + 0.5
        irrigations[(i + (grid_step * 3)) * HEIGHT + j] = (amount * timestep) + 0.5
        irrigations[(i + (grid_step * 4)) * HEIGHT + j] = (amount * timestep) + 0.5
        # irrigations[((grid_step)*4) * HEIGHT + j] = amount
        # print(irrigations)
        return irrigations

    return get_downhill_irrigation


def _make_row_irrigator(grid_step, amount, shift):
    def get_row_irrigation(timestep):
        # print("old timestep", timestep)
        row_max = WIDTH // grid_step
        col_max = HEIGHT // grid_step
        timestep = (timestep + shift) % (col_max)
        print("new timestep", timestep)
        row = timestep // col_max
        col = timestep % col_max
        print("row:", row, "col", col)
        i, j = row * grid_step + grid_step // 2, col * grid_step + grid_step // 2
        print("i:", row, "j", col)
        irrigations = [0] * (HEIGHT * WIDTH)
        irrigations[i * HEIGHT + j] = amount
        irrigations[(i + grid_step) * HEIGHT + j] = amount
        irrigations[(i + (grid_step * 2)) * HEIGHT + j] = amount
        irrigations[(i + (grid_step * 3)) * HEIGHT + j] = amount
        irrigations[(i + (grid_step * 4)) * HEIGHT + j] = amount
        # irrigations[((grid_step)*4) * HEIGHT + j] = amount
        # print(irrigations)
        return irrigations

    return get_row_irrigation


# def _make_downhill_irrigator(grid_step, amount, shift):
#     def get_downhill_irrigation(timestep):
#         row_max = WIDTH // grid_step
#         timestep = (timestep + shift) % row_max
#         row = timestep // row_max
#         # col = timestep % row_max
#         i, j = row * grid_step + grid_step // 2, row * grid_step + grid_step // 2
#         irrigations = [0] * (HEIGHT * WIDTH)
#         irrigations[i * HEIGHT + j] = amount
#         irrigations[i * HEIGHT + j] = amount
#         return irrigations
#     return get_downhill_irrigation

def _make_random_irrigator(amount):
    def get_irrigation(_):
        grid_size = HEIGHT * WIDTH
        irrigations = [0] * grid_size
        irrigations[np.random.randint(grid_size)] = amount
        # print(np.shape(irrigations))
        return irrigations

    return get_irrigation


# Creates different color plants in random locations
def _get_random_plants():
    PLANTS_PER_COLOR = 1

    #set3
    PLANT_TYPES = [((0, .39, 0), (0.13, 15), 'thyme'), ((.5, .55, .0), (0.11, 50), 'corn'), ((.49, .99, 0), (0.1, 25), 'basil')]


    # ((0, .6, 0), (0.13, 15), 'lettuce')]
    # PLANT_TYPES = [((.49, .99, 0), (0.1, 25), 'basil'), ((0, .39, 0), (0.13, 15), 'thyme')]

    np.random.seed(285631)
    plants = []
    for color, (w_effect, growth_time), type in PLANT_TYPES:
        x_locations = np.random.randint(1, HEIGHT - 1, (PLANTS_PER_COLOR, 1))
        y_locations = np.random.randint(1, WIDTH - 1, (PLANTS_PER_COLOR, 1))
        locations = np.hstack((x_locations, y_locations))
        plants.extend(
            [Plant(row, col, w_effect=w_effect, growth_time=growth_time, color=color, plant_type=type) for row, col in
             locations])
    return plants


def export_results(plants, logger, filename=None):
    """
  plants:   a list of Plant objects from this simulator run
  logger:   a Logger object with all collected data from this run
  filename: a string for the name of the file to save results to
  """
    if not filename:
        filename = time.strftime("%Y-%m-%d-%H%M%S")
    else:
        # Ignore any custom extensions
        filename = filename.split(".")[0]

    print(f"Exporting results to outputs/{filename}.json...")

    plant_data = []
    for plant in plants:
        plant_data.append({
            "type": plant.type,
            "radii": logger.get_data(Event.RADIUS_UPDATED, plant.id),
            "heights": logger.get_data(Event.HEIGHT_UPDATED, plant.id)
        })

    with open(f"./outputs/{filename}.json", "w+") as file:
        file.write(json.dumps(plant_data))

    print("Export complete.")


def read_results(filename):
    filename = filename.split(".")[0]
    with open(f"./outputs/{filename}.json") as file:
        data = json.load(file)
        return data


##############################
# SIMULATION RUN
##############################

def run_simulation(args):
    start_time = time.time()

    params = PLANT_PARAMS[args.setup]
    if params["seed"]:
        np.random.seed(params["seed"])
    plants = params["plants"]()
    daily_water = DAILY_WATER
    irrigation_policy = WATERING_SCHEDULE[args.irrigator]["policy"]() if args.irrigator in WATERING_SCHEDULE else lambda \
        _: None

    # Initialize the greenhouse
    # greenhouse = Greenhouse(plants, HEIGHT, WIDTH, SCALE, plant_types=['tomato', 'corn', 'lettuce'], animate=False)
    greenhouse = Greenhouse(plants, HEIGHT, WIDTH, SCALE, plant_types=['thyme', 'corn', 'basil'],
                            animate=(args.display == 'a'))

    # Run the simulation for FRAMES steps
    for i in range(FRAMES):
        plants = greenhouse.perform_timestep(water_amt=daily_water, irrigations=irrigation_policy(i))
        total_cc = np.sum(greenhouse.leaf_grid)
        cc_per_plant = [np.sum(greenhouse.leaf_grid[:, :, i]) for i in range(greenhouse.leaf_grid.shape[2])]
        print(cc_per_plant)
        prob = cc_per_plant / total_cc
        prob = prob[np.where(prob > 0)]
        entropy = -np.sum(prob * np.log(prob))
        print(entropy)

    print("--- %s seconds ---" % (time.time() - start_time))

    # Display either graphs of greenhouse data and the final greenhouse state, or a full animation of greenhouse timesteps
    if args.display == 'p':
        plot_data(greenhouse, FRAMES)
        plot_greenhouse(greenhouse)
    else:
        greenhouse.show_animation()

    # # Exports the plant data as a JSON file (for Helios visualization purposes)
    # if args.export:
    #     export_results(plants, greenhouse.logger, args.export)


def get_parsed_args():
    parser = argparse.ArgumentParser(description='Run the greenhouse simulation.')
    parser.add_argument('--setup', type=str, default='random',
                        help='Which plant setup to use. (`random` will place plants randomly across the greenhouse.)')
    parser.add_argument('--display', type=str, default='a',
                        help='[a|p] Whether to show full animation [a] or just plots of plant behaviors [p]')
    parser.add_argument('--irrigator', type=str, help='[uniform|sequential|downhill] The irrigation policy to use')
    parser.add_argument('--export', type=str, help='Name of file to save results to (if "none", will not save results)')
    return parser.parse_args()


args = get_parsed_args()
run_simulation(args)

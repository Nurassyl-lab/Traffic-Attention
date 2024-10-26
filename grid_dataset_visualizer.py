import pandas as pd
import argparse
from grid_maker import plot_grid
import numpy as np
from tqdm import tqdm
from utils.basic_functions import str2bool

# Load the dataset
def get_parser():
    parser = argparse.ArgumentParser(description='Visualize the grid dataset')
    parser.add_argument('--data_path', type=str, default='./data/grid_dataset/grid_dataset_fixed_direction.csv', help='Path to the data file')
    parser.add_argument('--collision_only', type=str2bool, default=True, help='Visualize only the samples with collision')
    return parser

if __name__ == '__main__':
    args = get_parser().parse_args()
    data_path = args.data_path

    df = pd.read_csv(data_path)

    for i in tqdm(range(len(df)), desc='Visualizing the dataset'):
        grid_size = df['grid_size'][i]
        object1_actions = df['object1_action'][i]
        object2_actions = df['object2_action'][i]
        collision_status = df['collision_status'][i]


        if args.collision_only and collision_status == 0:
            continue

        object1_actions = eval(object1_actions)
        object2_actions = eval(object2_actions)

        # create a grid
        matrix = np.zeros((grid_size, grid_size))
        for j, (obj1_pos, obj2_pos) in enumerate(zip(object1_actions, object2_actions)):
            plot_grid(grid_size, obj1_pos, obj2_pos, path=f'./data/grid_dataset_fixed_direction_images/sample{i+1}_frame{j}')
        
# Driver file for the data, datasets, dataloaders, and etc

import argparse
from grid_maker import GridMaker, plot_grid
import pandas as pd 
import numpy as np
from tqdm import tqdm

def get_parser():
    parser = argparse.ArgumentParser(description='Driver file for the data')
    parser.add_argument('--data', type=str, default='data.csv', help='Path to the data file')
    parser.add_argument('--num_samples', type=int, default=100, help='Number of samples to generate')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    # Display the arguments
    print(args)

    #TODO: Decide if we want to manage our data_driver this way
    # Long statements of if-else to determine which data to use
    # It will be easily readable, but a bit long in the future
    
    # 'grid_maker' is the data that we will use to test our "main" idea on a smaller scale
    # Data contains 10x10 grid with two objects (1 and 2)
    if args.data == 'grid_maker_random_directions':
        # Create a dictionary dataset
        dataset = {
            'grid_size': [],
            'object1_action': [],
            'object2_action': [],
            'collision_status': []
            }

        # Create a grid 
        grid_maker = GridMaker(grid_size=10, min_distance=3)
        
        grid_maker.create_grid()

        # use tqdm to display the progress bar
        for i in tqdm(range(args.num_samples), desc='Generating samples'):
            # Generate initial positions for the objects 
            object1_pos, object2_pos = grid_maker.place_rectangles()

            # Find the path for the objects to collide
            # or
            # Find the path for the objects to not collide
            # randomly generate max_length from 3 to 10

            #TODO: Move visualization part to grid_dataset_visualizer.py
            dataset['grid_size'].append(grid_maker.grid_size)
            if i % 2 == 0:
                object1_coll_actions, object2_coll_actions = grid_maker.find_path(object1_pos, object2_pos, randomness_factor=0.1)
                dataset['collision_status'].append(1)
                dataset['object1_action'].append(object1_coll_actions)
                dataset['object2_action'].append(object2_coll_actions)
                
                for j, (pos_1, pos_2) in enumerate(zip(object1_coll_actions, object2_coll_actions)):
                    grid_maker.grid.fill(0)
                    grid_maker.grid[pos_1] = 2
                    grid_maker.grid[pos_2] = 1
                    plot_grid(grid_maker.grid, pos_1, pos_1, path=f'./data/grid_dataset_images/sample{i+1}_frame{j}')

            else:
                max_length = np.random.randint(3, 10)
                object1_noncoll_actions, object2_noncoll_actions = grid_maker.find_non_collision_path(object1_pos, object2_pos, max_length=max_length, randomness_factor=0.1)
                dataset['collision_status'].append(0)
                dataset['object1_action'].append(object1_noncoll_actions)
                dataset['object2_action'].append(object2_noncoll_actions)

        # Save the dataset to a csv file
        df = pd.DataFrame(dataset)
        df.to_csv('./data/grid_dataset/grid_dataset.csv', index=False)

    elif args.data == 'grid_maker_fixed_direction':
        # Create a dictionary dataset
        dataset = {
            'grid_size': [],
            'object1_action': [],
            'object2_action': [],
            'collision_status': []
            }

        # Create a grid 
        grid_maker = GridMaker(grid_size=10, min_distance=3)
        
        grid_maker.create_grid()

        # use tqdm to display the progress bar
        for i in tqdm(range(args.num_samples), desc='Generating samples'):
            # Generate initial positions for the objects 
            object1_pos, object2_pos = grid_maker.place_rectangles()

            dataset['grid_size'].append(grid_maker.grid_size)
            
            object1_coll_actions, object2_coll_actions, collision = grid_maker.fix_direction_action()
            dataset['collision_status'].append(collision[0])
            dataset['object1_action'].append(object1_coll_actions)
            dataset['object2_action'].append(object2_coll_actions)

        # Save the dataset to a csv file
        df = pd.DataFrame(dataset)
        df.to_csv('./data/grid_dataset/grid_dataset_fixed_direction.csv', index=False)

    else:
        print(f'--data {args.data} is not supported')
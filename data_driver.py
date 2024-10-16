# Driver file for the data, datasets, dataloaders, and etc

import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='Driver file for the data')
    parser.add_argument('--data', type=str, default='data.csv', help='Path to the data file')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    # Display the arguments
    print(f'--data: {args.data}')

    #TODO: Decide if we want to manage our data_driver this way
    # Long statements of if-else to determine which data to use
    # It will be easily readable, but a bit long in the future
    
    # 'grid_data' is the data that we will use to test our "main" idea on a smaller scale
    # Data contains 10x10 grid with two objects (1 and 2)
    if args.data == 'grid_data':
        pass
    elif args.data == 'some_other_data':
        pass
    else:
        print(f'--data {args.data} is not supported')
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from matplotlib.animation import PillowWriter
import math 

# Wrap up all functoins below into a class
class GridMaker:
    def __init__ (self, grid_size, min_distance, flag=False):
        # Parameters
        self.grid_size = grid_size # size of the grid (grid_size x grid_size)
        self.min_distance = min_distance # initial distance between the two objects on the grid
        
        # flag for debugging
        self.flag = flag # flag to check if the initial positions of the objects are set

    def create_grid(self):
        """
        - Create a grid filled with zeros
        - All non-zero values will represent the objects on the grid
        """
        self.grid = np.zeros((self.grid_size, self.grid_size))

    def place_rectangles(self):
        """
        - Places two rectangles (blue and red) on a grid such that their positions
          are at least `min_distance` units apart based on Euclidean distance.
        """
        while True:
            blue_position = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
            red_position = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
            
            # Calculate Euclidean distance between the two positions
            distance = math.dist(blue_position, red_position)
            
            # Ensure the distance is at least `min_distance`
            if distance >= self.min_distance:
                if self.flag: 
                    print(f'Initial position: Blue {blue_position}, Red {red_position}')
                    print(f'Initial distance: {distance}\n')
                return blue_position, red_position

    def find_path(self, start_pos_blue, start_pos_red, randomness_factor=0.2):
        """
        - Creates movement patterns for both blue and red rectangles with some randomness added.
        - The patterns stop when both objects collide at the same coordinates.
          randomness_factor controls the likelihood of random movement at each step.
        """
        blue_pattern = []
        red_pattern = []

        blue_pattern.append(start_pos_blue)
        red_pattern.append(start_pos_red)
        
        current_blue = list(start_pos_blue)
        current_red = list(start_pos_red)
        
        while current_blue != current_red:
            # Randomize movement with a probability controlled by randomness_factor
            if random.random() < randomness_factor:
                # Move blue randomly
                direction = random.choice(['up', 'down', 'left', 'right'])
                if direction == 'up' and current_blue[0] > 0:
                    current_blue[0] -= 1
                elif direction == 'down' and current_blue[0] < self.grid_size - 1:
                    current_blue[0] += 1
                elif direction == 'left' and current_blue[1] > 0:
                    current_blue[1] -= 1
                elif direction == 'right' and current_blue[1] < self.grid_size - 1:
                    current_blue[1] += 1
            else:
                # Move blue towards red (efficient movement)
                if current_blue[0] < current_red[0]:
                    current_blue[0] += 1
                elif current_blue[0] > current_red[0]:
                    current_blue[0] -= 1

                if current_blue[1] < current_red[1]:
                    current_blue[1] += 1
                elif current_blue[1] > current_red[1]:
                    current_blue[1] -= 1

            # Randomize movement with a probability controlled by randomness_factor for red
            if random.random() < randomness_factor:
                # Move red randomly
                direction = random.choice(['up', 'down', 'left', 'right'])
                if direction == 'up' and current_red[0] > 0:
                    current_red[0] -= 1
                elif direction == 'down' and current_red[0] < self.grid_size - 1:
                    current_red[0] += 1
                elif direction == 'left' and current_red[1] > 0:
                    current_red[1] -= 1
                elif direction == 'right' and current_red[1] < self.grid_size - 1:
                    current_red[1] += 1
            else:
                # Move red towards blue (efficient movement)
                if current_red[0] < current_blue[0]:
                    current_red[0] += 1
                elif current_red[0] > current_blue[0]:
                    current_red[0] -= 1

                if current_red[1] < current_blue[1]:
                    current_red[1] += 1
                elif current_red[1] > current_blue[1]:
                    current_red[1] -= 1

            # Append current positions to the movement patterns
            blue_pattern.append(tuple(current_blue))
            red_pattern.append(tuple(current_red))

            # Stop if they collide
            if current_blue == current_red:
                break

        if self.flag:
            print(f'BLUE pattern:\n{blue_pattern}')
            print(f'RED pattern:\n{red_pattern}\n')
        return blue_pattern, red_pattern

    def find_non_collision_path(self, start_pos_blue, start_pos_red, max_length=10, randomness_factor=0.2):
        """
        - Creates movement patterns for both blue and red rectangles with some randomness added.
        - The patterns will not allow the objects to collide with each other.
        - The max_length parameter defines the maximum length of the movement patterns.
        randomness_factor controls the likelihood of random movement at each step.
        """
        blue_pattern = []
        red_pattern = []

        blue_pattern.append(start_pos_blue)
        red_pattern.append(start_pos_red)

        current_blue = list(start_pos_blue)
        current_red = list(start_pos_red)

        for _ in range(max_length):
            # Randomize movement for blue
            if random.random() < randomness_factor:
                direction = random.choice(['up', 'down', 'left', 'right'])
                if direction == 'up' and current_blue[0] > 0:
                    current_blue[0] -= 1
                elif direction == 'down' and current_blue[0] < self.grid_size - 1:
                    current_blue[0] += 1
                elif direction == 'left' and current_blue[1] > 0:
                    current_blue[1] -= 1
                elif direction == 'right' and current_blue[1] < self.grid_size - 1:
                    current_blue[1] += 1
            else:
                # Move blue in a random direction avoiding the red object
                if current_blue[0] < self.grid_size - 1 and current_blue[0] + 1 != current_red[0]:
                    current_blue[0] += 1
                elif current_blue[0] > 0 and current_blue[0] - 1 != current_red[0]:
                    current_blue[0] -= 1

                if current_blue[1] < self.grid_size - 1 and current_blue[1] + 1 != current_red[1]:
                    current_blue[1] += 1
                elif current_blue[1] > 0 and current_blue[1] - 1 != current_red[1]:
                    current_blue[1] -= 1

            # Randomize movement for red
            if random.random() < randomness_factor:
                direction = random.choice(['up', 'down', 'left', 'right'])
                if direction == 'up' and current_red[0] > 0:
                    current_red[0] -= 1
                elif direction == 'down' and current_red[0] < self.grid_size - 1:
                    current_red[0] += 1
                elif direction == 'left' and current_red[1] > 0:
                    current_red[1] -= 1
                elif direction == 'right' and current_red[1] < self.grid_size - 1:
                    current_red[1] += 1
            else:
                # Move red in a random direction avoiding the blue object
                if current_red[0] < self.grid_size - 1 and current_red[0] + 1 != current_blue[0]:
                    current_red[0] += 1
                elif current_red[0] > 0 and current_red[0] - 1 != current_blue[0]:
                    current_red[0] -= 1

                if current_red[1] < self.grid_size - 1 and current_red[1] + 1 != current_blue[1]:
                    current_red[1] += 1
                elif current_red[1] > 0 and current_red[1] - 1 != current_blue[1]:
                    current_red[1] -= 1

            # Append current positions to the movement patterns
            blue_pattern.append(tuple(current_blue))
            red_pattern.append(tuple(current_red))

            # Stop if the maximum length is reached
            if len(blue_pattern) >= max_length or len(red_pattern) >= max_length:
                break

        if self.flag:
            print(f'BLUE pattern:\n{blue_pattern}')
            print(f'RED pattern:\n{red_pattern}\n')

        return blue_pattern, red_pattern

# write a function that plot matrix with two objects
def plot_matrix(matrix, object1_loc, object2_loc, path):
    """
    - Plot the matrix with two objects
    """
    cmap = ListedColormap(['white', 'red', 'blue'])
    plt.matshow(matrix, cmap=cmap)
    plt.title('Grid with two objects')
    save_path = f'{path}.png'
    plt.savefig(save_path)
    plt.close()


class GridAnimator:
    def __init__(self, grid, blue_pattern, red_pattern, cmap):
        self.grid = grid
        self.blue_pattern = blue_pattern
        self.red_pattern = red_pattern

        # Create the figure and axis for plotting
        self.fig, self.ax = plt.subplots()
        self.mat = self.ax.matshow(self.grid, cmap=cmap)  # Create the matshow object

        # Create a text element for the frame number
        self.text = self.ax.text(0.05, 0.95, '', transform=self.ax.transAxes, fontsize=12, color='black',
                                 verticalalignment='top')

    def update_grid(self, frame):
        """
        - Update the grid for each frame of the animation
        """
        self.grid.fill(0)  # Clear the grid at each step

        if frame < len(self.blue_pattern):
            # Update blue position
            blue_pos = self.blue_pattern[frame]
            self.grid[blue_pos] = 2  # Set blue rectangle

        if frame < len(self.red_pattern):
            # Update red position
            red_pos = self.red_pattern[frame]
            self.grid[red_pos] = 1  # Set red rectangle

        # Update the plot
        self.mat.set_data(self.grid)

        # Update the frame number text
        self.text.set_text(f'Frame: {frame}')

        return [self.mat, self.text]

    def animate(self):
        # Create the animation
        ani = animation.FuncAnimation(
            self.fig, self.update_grid, frames=max(len(self.blue_pattern), len(self.red_pattern)),
            interval=500, blit=True
        )
        plt.show()


if __name__ == '__main__':
    """
    - Example usage of the GridMaker class
    """

    # Create an instance of the GridMaker class
    my_grid = GridMaker(grid_size=10, min_distance=3, flag=True)
    
    # Create a grid
    my_grid.create_grid()
    

    # Place objects on the grid
    # Color map for the grid
    cmap = ListedColormap(['white', 'red', 'blue'])
    
    # Find actions for the rectangles    
    for i in range(5):
        #! First animation will be empty, i think it's a bug

        print(f'Sample {i + 1}')
        blue_position, red_position = my_grid.place_rectangles()
        
        # find paths that leads to a collision
        # blue_actions, red_actions = my_grid.find_path(blue_position, red_position, randomness_factor=0.1)

        # find paths that leads to a non-collision
        blue_actions, red_actions = my_grid.find_non_collision_path(blue_position, red_position, max_length=10, randomness_factor=0.1)

        for pos_blue, pos_red in zip(blue_actions, red_actions):
            my_grid.grid.fill(0)# this line is added to clear the grid at each step
            my_grid.grid[pos_blue] = 2
            my_grid.grid[pos_red] = 1
            plot_matrix(my_grid.grid, pos_blue, pos_red)


        # for animation uncomment
        # cmap = ListedColormap(['white', 'red', 'blue'])

        # my_animation = GridAnimator(my_grid.grid, blue_actions, red_actions, cmap)

        # my_animation.animate()
     
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from matplotlib.animation import PillowWriter
import math 

def create_grid(size):
    return np.zeros((size, size))

def place_rectangle(grid_size, min_distance=3):
    """
    Places two rectangles (blue and red) on a grid such that their positions
    are at least `min_distance` units apart based on Euclidean distance.
    """
    while True:
        blue_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        red_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        
        # Calculate Euclidean distance between the two positions
        distance = math.sqrt((blue_position[0] - red_position[0])**2 + (blue_position[1] - red_position[1])**2)
        
        # Ensure the distance is at least `min_distance`
        if distance >= min_distance:
            return blue_position, red_position

def create_random_movement_pattern(start_pos_blue, start_pos_red, grid_size, randomness_factor=0.2):
    """
    Creates movement patterns for both blue and red rectangles with some randomness added.
    The patterns stop when both objects collide at the same coordinates.
    randomness_factor controls the likelihood of random movement at each step.
    """
    blue_pattern = []
    red_pattern = []
    
    current_blue = list(start_pos_blue)
    current_red = list(start_pos_red)
    
    while current_blue != current_red:
        # Randomize movement with a probability controlled by randomness_factor
        if random.random() < randomness_factor:
            # Move blue randomly
            direction = random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up' and current_blue[0] > 0:
                current_blue[0] -= 1
            elif direction == 'down' and current_blue[0] < grid_size - 1:
                current_blue[0] += 1
            elif direction == 'left' and current_blue[1] > 0:
                current_blue[1] -= 1
            elif direction == 'right' and current_blue[1] < grid_size - 1:
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
            elif direction == 'down' and current_red[0] < grid_size - 1:
                current_red[0] += 1
            elif direction == 'left' and current_red[1] > 0:
                current_red[1] -= 1
            elif direction == 'right' and current_red[1] < grid_size - 1:
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
    
    return blue_pattern, red_pattern

cmap = ListedColormap(['white', 'red', 'blue'])
# Function to update the grid for animation
def update_grid(frame, grid, blue_pattern, red_pattern, text):
    grid.fill(0)  # Clear the grid at each step
    
    if frame < len(blue_pattern):
        # Update blue position
        blue_pos = blue_pattern[frame]
        grid[blue_pos] = 2  # Set blue rectangle
    
    if frame < len(red_pattern):
        # Update red position
        red_pos = red_pattern[frame]
        grid[red_pos] = 1  # Set red rectangle
    
    # Update the plot
    mat.set_data(grid)

    # Update the frame number text
    text.set_text(f'Frame: {frame}')
    
    return [mat, text]


# Parameters
grid_size = 10

# Create a grid and place the rectangles
grid = create_grid(grid_size)
blue_position, red_position = place_rectangle(grid_size, min_distance=3)
print(f'BLUE initial position: {blue_position}')
grid[blue_position] = 2  # Mark blue rectangle with 2

print(f'RED initial position: {red_position}')
grid[red_position] = 1  # Mark red rectangle with 1

# Create movement patterns with randomness for both rectangles
blue_pattern, red_pattern = create_random_movement_pattern(blue_position, red_position, grid_size, randomness_factor=0.3)

print(f'RED pattern:\n{red_pattern}')
print(f'BLUE pattern:\n{blue_pattern}')

# Create the figure and axis for plotting
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap=cmap)

# Create a text element for the frame number
text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, color='black',
               verticalalignment='top')

# Create the animation
ani = animation.FuncAnimation(
    fig, update_grid, frames=max(len(blue_pattern), len(red_pattern)),
    fargs=(grid, blue_pattern, red_pattern, text), interval=500, blit=True
)
# Save the animation as a GIF
gif_writer = PillowWriter(fps=2)  # 2 frames per second (adjust as needed)
ani.save("data/grid_dataset/movement_animation.gif", writer=gif_writer)

# Display the animation
plt.show()

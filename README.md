# Content
- Description/Abstract
- How-to-RUN
- How does it work?
- Additional

# How-to-RUN

Do you want to try our code? Below, you can find a step-by-step guide that will show you how to do it.

Note that I use **Linux**, some of the steps may differ depending on OS.

### Requirements

- **Python** interpreter **python3**
	- Install **torch** from [link: PyTorch](https://pytorch.org/get-started/locally/)
	- Install other required packages using `pip install -r requirements.txt`


### Execution

- Run `grid_maker.py` using `python grid_maker.py`
- Run `data_driver.py` using `python data_driver.py --data grid_maker --num_samples 10000`

# How does it work?

Do you want to know how our code works? Below, you can find an overview of how it works.

### Grid Dataset Generation
- Using tools in `grid_maker.py` we can generate a NxN grid, $\text{N}\in \mathbb{Z}$. Grid is empty, filled with 0's. Then we randomly generate initial positions for 2 objects. Given the grid, and object positions, we now can generate their actions. It is possible to generate a colliding actions, and non-colliding.
- `data_driver.py` just wraps it up nicely and creates a `.csv` dataset.

### Data Pre-Processing

- Not Implemented yet
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

- **C++** compiler `g++ 4.8` and above
	- For data-visualization the **matplotlib** wrapper for **C++** is used. It's required to have **python** (*we only tested python3*) installed with **matplotlib** package.
	- Download a header file from [link: matplotlib-cpp github repository](https://github.com/lava/matplotlib-cpp/blob/master/matplotlibcpp.h)

- Additionally it's recommended to have 8GB of RAM, and 6GB of VRAM.

# How does it work?

Do you want to know how our code works? Below, you can find an overview of how it works.

### Data Pre-Processing

- To save time and to be more careful during pre-processing, this project implements **C++** in order to do data pre-processing.


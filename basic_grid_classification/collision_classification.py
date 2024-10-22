"""
Here we implement some basic classification techniques to classify the collision data.
We classify the data into 2 classes: collision and non-collision. 
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


# Goddamit



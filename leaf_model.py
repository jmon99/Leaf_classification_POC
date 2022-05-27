import matplotlib.pyplot as plt 
import numpy as np
import os
import tensorflow as tf

import tensorflow_datasets as tfds

#importing data
ds = tfds.load('plant_leaves', split='train', shuffle_files=True)
assert instance(ds, tf.data.Dataset)
print(ds)



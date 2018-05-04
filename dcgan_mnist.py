#encoding : utf-8

import numpy as np
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('/data')
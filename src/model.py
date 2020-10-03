import tensorflow as tf
import numpy as np
from tensorflow import keras
import os

class_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# different classification labels

path_to_images = "./training_images/"


model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu',
                              input_shape=(50, 50)), 
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(2, 2),
    # I applied 3 convolutional layers since hand data is quite complex and
    # we want to better extract those features from the images
    # 64 filters of a 3*3 filter with pools of 2*2
    # 3 convultions is a fair start to not over fit the model I figured

    keras.layers.Flatten(), 
    #current training images are 50 by 50, in final implementation will be 150 * 150
    # need to add max pooling layers to address this later
    keras.layers.Dense(128, activation=tf.nn.relu),
    # 128 is an arbitrary number of functions I chose from tutorial, same with the activation function
    keras.layers.Dense(36, activation=tf.nn.softmax)
    # 36 current characters that will be classified currently by this model (see class names)
    # activation is soft max since we want the character with the highest probability
])


model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
# Chose this optimizer and loss function from a tutorial video on image recognition



from keras import backend as K
from utility import LoadDataWTFPADCW
from Model_WTFPAD import DFNet
import random
from keras.utils import np_utils
from keras.optimizers import Adamax
import numpy as np
import os

random.seed(0)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Use only CPU
#os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
#os.environ["CUDA_VISIBLE_DEVICES"] = ""

description = "Training and evaluating DF model for closed-world scenario on WTF-PAD dataset"

print description
# Training the DF model
NB_EPOCH = 200   # Number of training epoch
print "Number of Epoch: ", NB_EPOCH
BATCH_SIZE = 128 # Batch size
VERBOSE = 2 # Output display mode
LENGTH = 2000 # Packet sequence length
OPTIMIZER = Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0) # Optimizer

NB_CLASSES = 100 # number of outputs = number of classes
INPUT_SHAPE = (LENGTH,1)


# Data: shuffled and split between train and test sets
print ("Loading and preparing data for training, and evaluating the model")
X_train, y_train, X_valid, y_valid, X_test, y_test = LoadDataWTFPADCW()
# Please refer to the dataset format in readme
K.set_image_dim_ordering("tf") # tf is tensorflow

# Convert data as float32 type
X_train = X_train.astype('float32')
X_valid = X_valid.astype('float32')
X_test = X_test.astype('float32')
y_train = y_train.astype('float32')
y_valid = y_valid.astype('float32')
y_test = y_test.astype('float32')

# we need a [Length x 1] x n shape as input to the DF CNN (Tensorflow)
X_train = X_train[:, :,np.newaxis]
X_valid = X_valid[:, :,np.newaxis]
X_test = X_test[:, :,np.newaxis]

print(X_train.shape[0], 'train samples')
print(X_valid.shape[0], 'validation samples')
print(X_test.shape[0], 'test samples')

# Convert class vectors to categorical classes matrices
y_train = np_utils.to_categorical(y_train, NB_CLASSES)
y_valid = np_utils.to_categorical(y_valid, NB_CLASSES)
y_test = np_utils.to_categorical(y_test, NB_CLASSES)

# Building and training model
print ("Building and training DF model")

model = DFNet.build(input_shape=INPUT_SHAPE, classes=NB_CLASSES)

model.compile(loss="categorical_crossentropy", optimizer=OPTIMIZER,
	metrics=["accuracy"])
print ("Model compiled")

# Start training
history = model.fit(X_train, y_train,
		batch_size=BATCH_SIZE, epochs=NB_EPOCH,
		verbose=VERBOSE, validation_data=(X_valid, y_valid))


# Start evaluating model with testing data
score_test = model.evaluate(X_test, y_test, verbose=VERBOSE)
print("Testing accuracy:", score_test[1])



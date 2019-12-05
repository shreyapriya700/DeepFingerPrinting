import pickle
import os
import numpy as np
from random import randint
import random
os.chdir("C:\Users\hp\Desktop\FCN Project\Deep Fingerprinting\closed-world-protected")

with open('good2.pickle', 'rb') as filehandle:
    # read the data as binary data stream
    classList = pickle.load(filehandle)
    i=0
with open('good1.pickle', 'rb') as filehandle:
    # read the data as binary data stream
    featurelist = pickle.load(filehandle)
    i=0

masterList=[]
X_train=[]
y_train=[]
X_valid=[]
y_valid=[]
X_test=[]
y_test=[]
for i in range(3933):
    masterList.append((featurelist[i],classList[i]))

random.shuffle(masterList)
T=masterList[:3200]
V=masterList[3200:3600]
Test=masterList[3600:]

for i in range(3200):
    X_train.append(T[i][0])
    y_train.append(T[i][1])
for i in range(400):
    X_valid.append(V[i][0])
    y_valid.append(V[i][1])
for i in range(333):
    X_test.append(Test[i][0])
    y_test.append(Test[i][1])

with open('X_train_NoDef' + '.pkl', 'wb') as f:
    pickle.dump(X_train, f)
with open('y_train_NoDef' + '.pkl', 'wb') as f1:
    pickle.dump(y_train, f1)
with open('X_valid_NoDef' + '.pkl', 'wb') as f2:
    pickle.dump(X_valid, f2)
with open('y_valid_NoDef' + '.pkl', 'wb') as f3:
    pickle.dump(y_valid, f3)
with open('X_test_NoDef' + '.pkl', 'wb') as f4:
    pickle.dump(X_test, f4)
with open('y_test_NoDef' + '.pkl', 'wb') as f5:
    pickle.dump(y_test, f5)





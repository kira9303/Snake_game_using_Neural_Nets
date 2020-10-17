import numpy as np
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

training_data = pickle.load(open('training_data.pkl','rb'))
train_x = pickle.load(open('train_x.pkl','rb'))
train_y = pickle.load(open('train_y.pkl','rb'))

#print(training_data)
training_data = np.array(training_data)
train_x = np.array(train_x)
train_y = np.array(train_y)
#print(training_data[3])
print("shape of the training data is:  {}".format(np.shape(training_data)))
print("shape of train_x is:  {}".format(np.shape(train_x)))
print("shape of train_y is:  {}".format(np.shape(train_y)))

x = []
y = []

for i in range(len(training_data)):
    if(i%2==0):
        x.append(training_data[i])
    else:
        y.append(training_data[i])
        
print(np.shape(x))

print(np.shape(y))

#print(train_x[0])
#print(train_y[0])

x = np.array(x)
y = np.array(y)

x = x / 500.0

print(x[2])
print(y[2])

print("shape is :   {}".format(np.shape(x[0])))
#print("length of train_x[0] is: {}".format(len(x[0])))



model = Sequential()
model.add(Dense(32, input_shape=(len(x[0]),), activation='relu'))
#model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.3))
#model.add(Dense(64, activation='relu'))
#model.add(Dropout(0.3))

#model.add(Dropout(0.5))
model.add(Dense(len(y[0]), activation='softmax'))

# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(lr=0.27, decay=1e-6, momentum=0.5, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#fitting and saving the model
hist = model.fit(x, y, epochs=1400, batch_size=500, verbose=1)
model.save('snake_train.h5', hist)
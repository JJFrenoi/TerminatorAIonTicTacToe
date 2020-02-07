import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam

training_data = np.array([[0,0,0,0],
	                      [0,0,1,0],
	                      [0,1,0,0],
	                      [0,1,0,1],
	                      [0,1,1,0],
	                      [1,0,0,0],
	                      [1,0,0,1],
	                      [1,0,1,0],
	                      [1,0,1,1],
	                      [1,1,0,0],
	                      [1,1,0,1],
	                      [1,1,1,0]], "float32")

target_data = np.array([[0],[2],[4],[5],[6],[8],[9],[10],[11],[12],[13],[14]], "float32")

model = Sequential()
model.add(Dense(1, input_dim=4, activation='relu'))

model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.05, beta_1=0.9, beta_2=0.999))

model.fit(training_data, target_data, nb_epoch=1500, verbose=2)

print (model.predict(training_data).round())

test_data = np.array([ [0,0,0,1],
	                   [0,0,1,1],
	                   [0,1,1,1],
	                   [1,1,1,1]], "float32")

print (model.predict(test_data).round())

for layer in model.layers:
    weights = layer.get_weights()
    print(weights)
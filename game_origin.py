#!/usr/bin/env python
# coding: utf-8


import numpy as np
import random

from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam

NB_STICKS = 21

model = Sequential()

model.add(Dense(units=32, input_shape=(1,), activation='sigmoid'))
model.add(Dense(units=32, activation='sigmoid'))
model.add(Dense(units=32, activation='sigmoid'))
model.add(Dense(units=1, activation='sigmoid'))

opt = Adam(lr=0.2, beta_1=0.9, beta_2=0.999)
model.compile(loss='binary_crossentropy', optimizer='adam',
              metrics=['binary_accuracy'])



def bestChoice(sticks):
    a = [1]
    if sticks >= 4:
        a = model.predict(np.array([sticks-1, sticks-2, sticks-3]))
    elif sticks == 3:
        a = model.predict(np.array([2, 1]))
    return np.argmax(a)+1


def PlayAiGame():
    sticks, player = NB_STICKS, random.randint(0, 2)
    states = []

    while sticks > 0:
        choice = bestChoice(sticks)
        states.append(sticks)
        sticks -= choice
        player = 1 - player

    won_or_lost = 0   # lost

    result = [None] * len(states)
    for i in reversed(range(len(result))):
        won_or_lost = 1 - won_or_lost
        result[i] = won_or_lost

    return np.array(states), np.array(result)

games, results = PlayAiGame()

for i in range(100):
    if i % 5 == 0:
        games, results = PlayAiGame()

    for j in range(20):
        g, r = PlayAiGame()
        games = np.append(games, g, axis=0)
        results = np.append(results, r, axis=0)

    model.fit(games, results, epochs=100, validation_split=0.5)

    print('Generation :', i)
    for k in range(1, 22):
        print("       ", k, " : ", bestChoice(
            k), model.predict(np.array([k]))[0])

    #print(PlayAiGame())

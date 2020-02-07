from iSenseiGame import *
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.backend import reshape
from keras.utils.np_utils import to_categorical
import numpy as np

def getModel():
    numCells = 49
    outcomes = 3
    model = Sequential()
    model.add(Dense(1100, activation='relu', input_shape=(numCells, )))
    model.add(Dropout(0.2))
    model.add(Dense(685, activation='relu'))
    model.add(Dense(405, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(135, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(75, activation='relu'))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(outcomes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['acc'])
    return model
def gamesToWinLossData(games):
    X = []
    y = []
    for game in games:
        result_player_1 = game.check_win_by_points (True)
        result_player_2 = game.check_win_by_points (False)
        if result_player_1 > result_player_2:
            winner = 1
        elif result_player_2 > result_player_1:
            winner = 2
        else :
            continue
        for move in range(49):
            X.append(game.board)
            y.append(winner)

    X = np.array(X).reshape((-1, 49))
    y = to_categorical(y)
    
    # Return an appropriate train/test split
    trainNum = int(len(X) * 0.8)
    return (X[:trainNum], X[trainNum:], y[:trainNum], y[trainNum:])

model = getModel()

X = []
y = []
for i in range(2):
    iSensei = iSensei("bender","terminator_2")
    result_player_1 = iSensei.check_win_by_points (True)
    print("O:%s"%result_player_1)
    result_player_2 = iSensei.check_win_by_points (False)
    print("X:%s"%result_player_2)
    if result_player_1 > result_player_2:
        winner = 1
    elif result_player_2 > result_player_1:
        winner = 2
    elif result_player_1 == result_player_2:
        winner = 0
    else:
        continue
        
    for move in range(49):
        X.append(iSensei.board)
        y.append(winner)
    print("bender vs terminator_2 %s/10000"%i)
for i in range(2):
    iSensei = iSensei("c3po","terminator_2")
    result_player_1 = iSensei.check_win_by_points (True)
    print("O:%s"%result_player_1)
    result_player_2 = iSensei.check_win_by_points (False)
    print("X:%s"%result_player_2)
    if result_player_1 > result_player_2:
        winner = 1
    elif result_player_2 > result_player_1:
        winner = 2
    elif result_player_1 == result_player_2:
        winner = 0
    else:
        continue
        
    for move in range(49):
        X.append(iSensei.board)
        y.append(winner)
    print("c3po vs terminator_2 %s/10000"%i)
for i in range(10000):
    iSensei = iSensei("terminator","terminator_copy")
    result_player_1 = iSensei.check_win_by_points (True)
    print("1:%s"%result_player_1)
    result_player_2 = iSensei.check_win_by_points (False)
    print("2:%s"%result_player_2)
    if result_player_1 > result_player_2:
        winner = 1
    elif result_player_2 > result_player_1:
        winner = 2
    elif result_player_1 == result_player_2:
        winner = 0
    else:
        continue
        
    for move in range(49):
        X.append(iSensei.board)
        y.append(winner)
    print("terminator vs terminator_copy %s/10000"%i)
for i in range(10000):
    iSensei = iSensei("bender","terminator")
    result_player_1 = iSensei.check_win_by_points (True)
    print("1:%s"%result_player_1)
    result_player_2 = iSensei.check_win_by_points (False)
    print("2:%s"%result_player_2)
    if result_player_1 > result_player_2:
        winner = 1
    elif result_player_2 > result_player_1:
        winner = 2
    elif result_player_1 == result_player_2:
        winner = 0
    else:
        continue
        
    for move in range(49):
        X.append(iSensei.board)
        y.append(winner)
    print("bender vs terminator %s/10000"%i)
for i in range(10000):
    iSensei = iSensei("terminator","c3po")
    result_player_1 = iSensei.check_win_by_points (True)
    print("1:%s"%result_player_1)
    result_player_2 = iSensei.check_win_by_points (False)
    print("2:%s"%result_player_2)
    if result_player_1 > result_player_2:
        winner = 1
    elif result_player_2 > result_player_1:
        winner = 2
    elif result_player_1 == result_player_2:
        winner = 0
    else:
        continue
        
    for move in range(49):
        X.append(iSensei.board)
        y.append(winner)
    print("terminator vs c3po %s/10000"%i)
    
for i in range(10000):
    iSensei = iSensei("bender","c3po")
    result_player_1 = iSensei.check_win_by_points (True)
    print("1:%s"%result_player_1)
    result_player_2 = iSensei.check_win_by_points (False)
    print("2:%s"%result_player_2)
    if result_player_1 > result_player_2:
        winner = 1
    elif result_player_2 > result_player_1:
        winner = 2
    elif result_player_1 == result_player_2:
        winner = 0
    else:
        continue
        
    for move in range(49):
        X.append(iSensei.board)
        y.append(winner)
    print("bender vs c3po %s/10000"%i)


X = np.array(X).reshape((-1, 49))
y = to_categorical(y)
    
# Return an appropriate train/test split
trainNum = int(len(X) * 0.8)

X_train, X_test, y_train, y_test =  (X[:trainNum], X[trainNum:], y[:trainNum], y[trainNum:]) #gamesToWinLossData(games)
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=50)
model.save("termi_Ai.model")
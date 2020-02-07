from random import *
import tensorflow as tf
import numpy as np 
# Init your variables here 
terminator_model = tf.keras.models.load_model("termi_Ai.model")
# Put your bot name here
name = "TERMINATOR 2"
# C3PO strategy : return random available celle 

def play(board, available_cells, player):
    scores = []
    moves = available_cells
    for move in moves:
        future = np.array(board)
        future[move] = player
        prediction = terminator_model.predict(future.reshape((-1,49)))[0]
        if player == 1 :
            winPrediction = prediction[1]
            lossPrediction = prediction[2]
        else:
            winPrediction = prediction[2]
            lossPrediction = prediction[1]
        drawPrediction = prediction[0]
        if winPrediction - lossPrediction > 0:
            scores.append(winPrediction -lossPrediction)
        else:
            scores.append(drawPrediction-lossPrediction)
    bestMoves = np.flip(np.argsort(scores))
    if len(bestMoves)>0 :
        return moves[bestMoves[0]]
    else: 
        return moves[random.randint(0, len(moves) - 1)]
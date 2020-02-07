from iSenseiGame import *
#iSensei = iSensei()
stats = {"win_player_1": 0,"win_player_2":0, "loss_player_1": 0,"loss_player_2":0, "draw": 0}
nbOfgame = 100
for i in range(100):
    iSensei = iSensei("c3po","terminator_2")
    result_player_1 = iSensei.check_win_by_points (False)
    print("playerX: %s"%result_player_1)
    result_player_2 = iSensei.check_win_by_points (True)
    print("player0: %s"%result_player_2)
    if result_player_1 == -1 or result_player_2 == -1:
        continue
    elif result_player_1 > result_player_2:
        stats["win_player_1"] += 1
        stats["loss_player_2"] +=1
    elif result_player_2 > result_player_1 :
        stats["win_player_2"] += 1
        stats["loss_player_1"] +=1
    elif result_player_1 == result_player_2:
        stats["draw"]+=1
                
win_player_1_Pct = stats["win_player_1"] / nbOfgame * 100
win_player_2_Pct = stats["win_player_2"] / nbOfgame * 100
loss_player_1_Pct = stats["loss_player_1"] / nbOfgame * 100
loss_player_2_Pct = stats["loss_player_2"] / nbOfgame * 100
drawPct = stats["draw"] / nbOfgame * 100

print("Results for player 1 ")
print("Wins: %d (%.1f%%)" % (stats["win_player_1"], win_player_1_Pct))
print("Loss: %d (%.1f%%)" % (stats["loss_player_1"], loss_player_1_Pct))
print("Draw: %d (%.1f%%)" % (stats["draw"], drawPct))
print()
print("Results for player 2 ")
print("Wins: %d (%.1f%%)" % (stats["win_player_2"], win_player_2_Pct))
print("Loss: %d (%.1f%%)" % (stats["loss_player_2"], loss_player_2_Pct))
print("Draw: %d (%.1f%%)" % (stats["draw"], drawPct))


def gameStats(games):
    
    for i in range(len(games)):
        
        result_player_1 = games[i].check_win_by_points (False)
        print("playerX: %s"%result_player_1)
        result_player_2 = games[i].check_win_by_points (True)
        print("player0: %s"%result_player_2)
        if result_player_1 == -1 or result_player_2 == -1:
            continue
        elif result_player_1 > result_player_2:
            stats["win_player_1"] += 1
            stats["loss_player_2"] +=1
        elif result_player_2 > result_player_1 :
            stats["win_player_2"] += 1
            stats["loss_player_1"] +=1
        elif result_player_1 == result_player_2:
            stats["draw"]+=1
                
    win_player_1_Pct = stats["win_player_1"] / len(games) * 100
    win_player_2_Pct = stats["win_player_2"] / len(games) * 100
    loss_player_1_Pct = stats["loss_player_1"] / len(games) * 100
    loss_player_2_Pct = stats["loss_player_2"] / len(games) * 100
    drawPct = stats["draw"] / len(games) * 100

    print("Results for player 1 ")
    print("Wins: %d (%.1f%%)" % (stats["win_player_1"], win_player_1_Pct))
    print("Loss: %d (%.1f%%)" % (stats["loss_player_1"], loss_player_1_Pct))
    print("Draw: %d (%.1f%%)" % (stats["draw"], drawPct))
    print()
    print("Results for player 2 ")
    print("Wins: %d (%.1f%%)" % (stats["win_player_2"], win_player_2_Pct))
    print("Loss: %d (%.1f%%)" % (stats["loss_player_2"], loss_player_2_Pct))
    print("Draw: %d (%.1f%%)" % (stats["draw"], drawPct))

"""gameStats(games)"""
def gameStats2(games):
    stats = {"win_player_1": 0,"win_player_2":0, "loss_player_1": 0,"loss_player_2":0, "draw": 0}
    for game in games:
        if game.check_win(game.lastPosition,False):
            stats["win_player_1"] += 1
            stats["loss_player_2"] +=1
        elif game.check_win(game.lastPosition,True):
            stats["win_player_2"] += 1
            stats["loss_player_1"] +=1
        else:
            stats["draw"]+=1
            
                
    win_player_1_Pct = stats["win_player_1"] / len(games) * 100
    win_player_2_Pct = stats["win_player_2"] / len(games) * 100
    loss_player_1_Pct = stats["loss_player_1"] / len(games) * 100
    loss_player_2_Pct = stats["loss_player_2"] / len(games) * 100
    drawPct = stats["draw"] / len(games) * 100

    print("Results for player 1 ")
    print("Wins: %d (%.1f%%)" % (stats["win_player_1"], win_player_1_Pct))
    print("Loss: %d (%.1f%%)" % (stats["loss_player_1"], loss_player_1_Pct))
    print("Draw: %d (%.1f%%)" % (stats["draw"], drawPct))
    print()
    print("Results for player 2 ")
    print("Wins: %d (%.1f%%)" % (stats["win_player_2"], win_player_2_Pct))
    print("Loss: %d (%.1f%%)" % (stats["loss_player_2"], loss_player_2_Pct))
    print("Draw: %d (%.1f%%)" % (stats["draw"], drawPct))

#gameStats(games)
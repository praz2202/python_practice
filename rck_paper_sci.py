import sys
print('Choose from rock, paper and scissors')

while True:
    dict_game ={'rock':1,'scissors':2,'paper':3}

    player1 = raw_input('player1, enter your option:\n')
    player1 = str(player1)
    player2 = raw_input('player1, enter your option:\n')
    player2 = str(player2)

    as1 = dict_game[player1]
    as2 = dict_game[player2]
    dif = as1-as2

    if dif ==-1 or dif ==2:
        print('Player1 wins the game')
    elif dif ==0:
        print('it is a tie game')
    else:
        print('Player2 wins the game')

    start = raw_input('Do you want start again?(y/n)\n')
    start = str(start)
    if start =='y':
        print('\nOk, restarting ...')
    else:
        print('\ngame over')
        break



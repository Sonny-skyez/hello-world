'''
Game of war (beggar-my-neighbour):
a card game for two players in which the object is to win all of the other player's cards.
Enjoy!

Written: 14.11.2018 r.
Author: Chris Brymer
'''

import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

random.shuffle(allCards)
print(allCards)
player1 = allCards[:12]
player2 = allCards[12:]
print('--------PLAYER 1--------')
print(player1)
print('--------PLAYER 2--------')
print(player2)
print('------------------------')

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    stock = []
    stock.append(card1)
    stock.append(card2)
    if card1['Power'] == card2['Power']:     
        while len(player1) > 0 and len(player2) > 0:
            print('WOJNA!!')   
            card3 = player1.pop(0)
            card4 = player2.pop(0)
            if len(player1) == 0:
               print('Wojne wygrywa PLAYER 2. P1 =',len(player1),'P2 =',len(player2))
               break
            elif len(player2) == 0:
                print('Wojne wygrywa PLAYER 1. P1 =',len(player1),'P2 =',len(player2))
            else:                
                card5 = player1.pop(0)
                card6 = player2.pop(0)
                stock.append(card3)
                stock.append(card4)
                stock.append(card5)
                stock.append(card6)         
                if card5['Power'] > card6['Power']:
                    player1.extend(stock)
                    print('Wojne wygrywa PLAYER 1. P1 =',len(player1),'P2 =',len(player2))
                    break                
                elif card5['Power'] < card6['Power']:
                    player2.extend(stock)
                    print('Wojne wygrywa PLAYER 2. P1 =',len(player1),'P2 =',len(player2))
                    break
                else:
                    if len(player2) == 0:
                        print('PLAYER 1 WON THE GAME!!!! P1 =',len(player1),'P2 =',len(player2))
                        break
                    elif len(player1) == 0:
                        print('PLAYER 1 WON!!!! P1 =',len(player1),'P2 =',len(player2))
                        break
                    else:
                        if len(player1) == 1 or len(player1) == 0:
                            print('PLAYER 2 WON THE GAME!!!! P1 =',len(player1),'P2 =',len(player2))
                            break
                        elif len(player2) == 1 or len(player2) == 0:
                            print('PLAYER 1 WON THE GAME!!!! P1 =',len(player1),'P2 =',len(player2))
                            break
                        else:
                            print('Remis wojny! Dogrywka! P1 =',len(player1),'P2 =',len(player2))
                            continue       
        if len(player2) == 0:
            break
        elif len(player1) == 0:
            break
        else:
            continue          
    elif card1['Power'] > card2['Power']:        
        player1.append(card1)
        player1.append(card2)       
        print('PLAYER 1 WON! Cards left P1: %d P2: %d' % (len(player1),\
                                                          len(player2)))                                                                                                                                                                                                    
    else:        
        player2.append(card2)
        player2.append(card1)      
        print('PLAYER 2 WON! Cards left P1: %d P2: %d' % (len(player1),\
                                                          len(player2)))
      
if len(player1) > 0:
    print('PLAYER 1 WON THE GAME!!!!')
else:
    print('PLAYER 2 WON THE GAME!!!!')

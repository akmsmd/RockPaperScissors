from ast import And, IsNot
import random

options = ['R','P', 'S']
print('Rock: R, Paper: P, Scissor: S')
cpu = random.choice(options)
#random.choice(options)
player = None
while player not in options:
  player = input('Choose one of these options: R/P/S: ').upper()
  if player == cpu:
    print('You have chosen: '+ player)
    print('Computer has chosen: '+ cpu)
    print('It is a tie!')
    player = input('Choose one of these options: R/P/S: ').upper()
    
if player == 'R':
    if cpu == 'P':
        print('Player has chosen: '+ player)
        print('Computer has chosen: '+ cpu)
        print('Computer wins!')
    if cpu == 'S'  :
        print('Player has chosen: '+ player)
        print('Computer has chosen: '+ cpu)
        print('Player wins!')
elif player == 'P':
    if cpu == 'S':
        print('Player has chosen: '+ player)
        print('Computer has chosen: '+ cpu)
        print('Computer wins!')
    if cpu == 'R'  :
        print('Player has chosen: '+ player)
        print('Computer has chosen: '+ cpu)
        print('Player wins!')  
elif player == 'S':
    if cpu == 'R':
        print('Player has chosen: '+ player)
        print('Computer has chosen: '+ cpu)
        print('Computer wins!')
    if cpu == 'P'  :
        print('Player has chosen: '+ player)
        print('Computer has chosen: '+ cpu)
        print('Player wins!')                


  
  
  
    
    


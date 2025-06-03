def print_game(lst):
    a='''
    {}|{}|{}
   ----------
    {}|{}|{}
   ----------
    {}|{}|{}'''.format(*lst)
    print(a)
choices=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
print("Welcome to tic tak toe game")
print_game(choices)
turns='X'
while " " in choices:
    t=int(input(f'Its your turn {turns} please enter :'))  
    if (choices[0]==choices[1]==choices[2]!=' ') or (choices[3]==choices[4]==choices[5]!=' ') or (choices[6]==choices[7]==choices[8]!=' ') or (choices[0]==choices[3]==choices[6]!=' ') or (choices[1]==choices[4]==choices[7]!=' ') or (choices[2]==choices[5]==choices[8]!=' ') or (choices[0]==choices[4]==choices[8]!=' ') or (choices[2]==choices[4]==choices[6]!=' '):    
        print(f'You Won {turns}')
    else:
        print("You Won {turns} ")
    


    if choices[t]==" ":
        choices[t]=turns
        turns="X" if turns=='0' else '0'
    else:
        print("Your turn dismissed")
        turns="X" if turns=='0' else '0'
    
    print_game(choices)
else:
    print("Tie")
    print("Game Ended")




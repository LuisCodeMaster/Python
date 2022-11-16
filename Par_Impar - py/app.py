from random import randint
print("Welcome to Impar or Par game!!")
v = 0

while True:
    player = int(input('Bet your value: '))
    computer =  randint(0, 10)
    total = player + computer
    type = " "
    while type not in 'PI':
        type = str(input('Par or impar? [P/I]')).strip().upper()[0]
    print(f'You played {player} and teh computer {computer}, Total of {total}', end = ' ')
    print('It got PAR' if total % 2  == 0 else 'It got IMPAR')
    if type == 'P':
        if total % 2 == 0:
            print('You win!')
            v += 1
        else:
         print('You lose!')
         break
    elif type  == 'I':
        if total  % 2 == 1:
            print('You win!')
            v += 1
        else:
            print('You lose!')
            break
        print('Lets play again...')
print(f"GAME OVER!  You won {v} time" if v == 1 else f"GAME OVER!  You won {v} times")
        
         
            
        
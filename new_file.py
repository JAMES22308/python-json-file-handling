
def ask(prompt):
    asking = input(prompt)
    return asking

def car_game():
    print("-----------CAR GAME-----------")
    print('ai is talking...')
    running = False
    while True:
        option = ask('press 1 to start | press 2 to stop | press 3 to exit: ')
        if option == '1':
            if running:
                print('engine is already running')
            else:
                print('engine started')
                running = True
        elif option == '2':
            if not running:
                print("engine is already stopped")
            else:
                print('engine is stopped')
                running = False
        elif option == '3':
            print('-----------GAME OVER!-----------')
            break
        else:
            print('try again')
            

car_game()
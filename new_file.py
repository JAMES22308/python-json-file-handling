print("-----------CAR GAME-----------")
running = False
while True:
    option = input('type start to start | type stop to stop | type exit to exit: ')
    if option == 'start':
        if running:
            print('engine is already running')
            print('engine is already running')
        else:
            print('engine started')
            print('engine started')
            running = True
    elif option == 'stop':
        if not running:
            print("engine is already stopped")
            print("engine is already stopped")
        else:
            print('engine is stopped')
            print('engine is stopped')
            running = False
    elif option == 'exit':
        print('-----------GAME OVER-----------')
        print('-----------GAME OVER-----------')

    else:
        print('try again')
        print('try again')
        


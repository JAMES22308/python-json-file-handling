running = False
while True:
    option = input('press 1 to start | press 2 to stop: ')
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
        print('bye')
        break
    else:
        print('try again')


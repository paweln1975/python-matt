
input = MagicMock(side_effect=['0', '9', '1', '8', '2', '7', '3', '6', '4'])
current = 0
found = False

while current < MAX_TRIES:
    current += 1
    guess = input('\nType number: ')

    if int(guess) > HIDDEN:
        print('Above')
    elif int(guess) < HIDDEN:
        print('Below')
    else:
        print('Exactly')
        break

if not found:
    print('Game over, max tries achieved.')

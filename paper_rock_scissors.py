import random

option = ['rock', 'paper', 'scissors']


def partida(user, machine):
    if user == machine:
        result = 'Tied'
    elif user == 'rock':
        if machine == 'scissors':
            result = 'User Winner'
        else:
            result = 'Machine Winner'
    elif user == 'paper':
        if machine == 'rock':
            result = 'User Winner'
        else:
            result = 'Machine Winner'
    else:
        if machine == 'paper':
            result = 'User Winner'
        else:
            result = 'Machine Winner'
    return result


def initial(user):
    if user == '1':
        option_user = option[0]
    elif user == '2':
        option_user = option[1]
    else:
        option_user = option[2]
    return option_user

def main():
    while True:
        input_user = input("Digite (1) Piedra, (2) Papel ó (3) Tijeras (q) Salir ")
        if input_user.lower() == 'q':
            break
        else:
            try:
                if (int(input_user) >= 1) and (int(input_user) <= 3):
                    option_user = initial(input_user)
                    number_random = random.randint(0, 2)
                    option_machine = option[number_random]
                    winner = partida(option_user, option_machine)
                    print(f'user: {option_user} vs machine: {option_machine}')
                    print(winner)
                else:
                    print('Por favor digita una opcion valida')
            except ValueError:
                print('Por favor digita una opcion valida')


if __name__ == '__main__':
    main()

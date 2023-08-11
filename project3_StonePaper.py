import random as r


def game():
    l = ['Stone🗻', 'Paper📃', 'Scissor✂']
    round = 0
    UserPoint = 0
    ComputerPoint = 0

    while True:
        user = getvalue(
            "\n(1)-> Stone\n(2)-> Paper\n(3)-> Scissor\n(4)----------------> Quit Game\n====>", 4)

        if user == 4:
            if round != 0:
                print(
                    "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(
                    '''                        GAME RESULT                                 ''')
                print(
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(
                    f"\nTotal Round : {round}\nYour Score : {UserPoint}\nOponents Score : {ComputerPoint}\nTie : {round-(UserPoint+ComputerPoint)}")
                print(
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
            else:
                break

        else:
            user = l[user-1]
            com = r.choice(l)

            if user == com:
                print(f"\n-> T I E ( {user}  over {com} )")

            elif user == 'Stone🗻' and com == 'Scissor✂':
                print(f"\nYou Win --> ( {user}  Breaks {com} )")
                UserPoint += 1

            elif user == 'Paper📃' and com == 'Stone🗻':
                print(f"\nYou Win --> ( {user}  Covers {com} )")
                UserPoint += 1

            elif user == 'Scissor✂' and com == 'Paper📃':
                print(f"\nYou Win --> ( {user}  Cuts {com} )")
                UserPoint += 1

            else:
                print(f"\nYou Loss --> ( {user}  Loose from {com} )")
                ComputerPoint += 1
        round += 1


def getvalue(Text, limit):
    while True:
        try:
            value = int(input(Text))
            if value < 1 or value > limit:
                print("\nValue should be Valid")
            else:
                return value

        except ValueError:
            print("\nInvalid Input (Only Integers Allowed)")


game()
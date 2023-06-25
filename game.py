from character import Character 
from random import randint

def view_status(player):
    print(f'{5*"-"} PLAYER STATUS {5*"-"}')
    [print(f'{key.upper()}: {value}') for key, value in player.__dict__.items()]
    print(25*"-")


def is_alive(player):
    if (player.hp <= 0):
        return False
    else:
        return True


def calc_damage(attacker, defender):
    damage = (attacker.attack * 2) - (defender.defense / 2)
    return damage


def get_first_player():
    return randint(0, 1)


def swap_player_turn(player):
    return 0 if player == 1 else 1


def battle(p1, p2):
    players = [p1, p2]

    has_winner = False
    attacker = get_first_player()
    defender = 0 if attacker == 1 else 1

    while has_winner == False:
        print(20*'-')
        print(f'{players[attacker].name} turn!')
        damage = calc_damage(players[attacker], players[defender])
        print(f'Damage: {damage}')
        players[defender].hp -= damage
        print(f'{players[defender].name} HP: {players[defender].hp}')
        has_winner = True if is_alive(players[defender]) == False else False
        if not has_winner:
            attacker = swap_player_turn(attacker)
            defender = 0 if attacker == 1 else 1
    else:
        print(f'Winner: {players[attacker].name}!')
    


if __name__ == "__main__":
    name = input('Hello traveler! What is your name?\n')
    p2_name = 'Monster'

    player_one = Character(name)
    player_two = Character(p2_name)

    print(f'Welcome to the Dungeon Explorer, {player_one.name}!\n')

    view_status(player_one)
    view_status(player_two)

    battle(player_one, player_two)

    '''
    Scope:
        Damage variance;
        Critical damage;
        Evasive;
        Run away;
        Skills;
        Skill points;
        Battle start rate;
        XP;
        Level up;
        Classes;
    '''
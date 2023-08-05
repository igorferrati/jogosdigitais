import random
import time

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 50
        self.armor = 60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEAD)" % self.name

    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -= 20
        print(self.name, "is hit")
        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")


def create_tank():
    tanks = {}
    while True:
        qtd = int(input('Quantos tanques vão jogar?[2/10]: '))
        if qtd < 2 or qtd > 10:
            print('Quantidade invalida!!, digite de 2 a jogadores!')
        else:
            break

    for i in range(qtd):
        name = input(f'Nome do {i+1}° TANQUE: ')
        tanks[chr(65 + i)] = Tank(name)

    return tanks


def player_info():
    for tank in tanks.values():
        print(tank)

print(f'{"*" * 25} Batalha de Tanques {"*" * 25}\n')
print(f'{"_" * 18} Cada jogador deve criar um tanque! {"_" * 18}\n')

tanks = create_tank()
players = list(tanks.keys())

while len(tanks) > 1:
    alive_players = [player for player in tanks if tanks[player].alive]
    random.shuffle(alive_players)

    for current_player in alive_players:
        if not tanks[current_player].alive:
            continue

        print(f'{"_" * 25} Informações dos Jogadores ! {"_" * 25}\n')
        player_info()
        print(f'{"_" * 50}\n')

        print("Sorteando...\n")
        time.sleep(2)

        print(f"{tanks[current_player]} sorteado! fará um ataque!\n")

        print(f"Escolha o alvo para ataque!\n")
        enemy_players = {k: tanks[k] for k in tanks if k != current_player and tanks[k].alive}
        for key, enemy in enemy_players.items():
            print(f"{key}: {enemy}")

        while True:
            target_key = input(f'{tanks[current_player].name}, escolha o alvo ({" ".join(enemy_players.keys())}): ').upper()
            if target_key in enemy_players and enemy_players[target_key].alive:
                break
            else:
                print("Escolha inválida! Digite uma chave válida.")

        target = enemy_players[target_key]

        print(f"{tanks[current_player]} ATACA {target}")
        tanks[current_player].fire_at(target)
        print(f'{"-" * 70}\n')

        if not target.alive:
            print(f" {target} fora do jogo!")
            tanks.pop(target_key)
            print(f'{"-" * 70}\n')

winner = tanks[list(tanks.keys())[0]]
print(f"VENCEDOR: {winner.name}")

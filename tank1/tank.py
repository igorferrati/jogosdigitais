import time
import random

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
        try:
            qtd = int(input('Quantos tanques vão jogar?[2/10]: '))
            if not 2 <= qtd <= 10:
                print('Quantidade inválida! Digite um valor entre 2 e 10.')
            else:
                break
        except ValueError:
            print('Entrada inválida! Digite um número inteiro válido.')

    for i in range(qtd):
        name = input(f'Nome do {i+1}° TANQUE: ')
        tanks[chr(65 + i)] = Tank(name)

    return tanks


def player_info():
    for tank in tanks.values():
        print(tank)


#game
print(f'{"*" * 25} Batalha de Tanques {"*" * 25}')
print(f'Cada jogador deve criar um tanque!!!\n')

tanks = create_tank()
players = list(tanks.keys())

while len(tanks) > 1:
    round = 0
    current_player = random.choice(players)
    tank = tanks[current_player]

    if not tank.alive:
        continue

    print(f'{"_" * 70}\n')
    print(f'Status dos jogadores:')
    time.sleep(1)
    player_info()
    print(f' \n')

    print(f'{"*" *30} Round: {round} {"*" *30}')
    print("Sorteando...")
    time.sleep(2)

    print(f"{tank.name} sorteado! fará um ataque!!")

    enemy_players = {k: tanks[k] for k in tanks if k != current_player and tanks[k].alive}
    if not enemy_players:
        break

    print(f"Escolha o alvo para ataque!\n")
    for key, enemy in enemy_players.items():
        print(f"{key}: {enemy}")

    while True:
        target_key = input(f'{tank.name}, escolha o alvo ({" ".join(enemy_players.keys())}): ').upper()
        if target_key in enemy_players and enemy_players[target_key].alive:
            break
        else:
            print("Escolha inválida! Digite uma chave válida.")

    target = enemy_players[target_key]

    print(f"{tank.name} ATACA {target.name}")
    tank.fire_at(target)

    if not target.alive:
        print(f"{target} fora do jogo!")
        tanks.pop(target_key)
        players.remove(target_key)
    
    round += 1

winner = tanks[list(tanks.keys())[0]]
print(f"VENCEDOR: {winner.name}")
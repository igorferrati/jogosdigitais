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
        qtd = int(input('Quantos tanques vão jogar?[2/10]: '))
        if qtd < 2 or qtd > 10:
            print('Quantidade invalida!!, digite de 2 a jogadores!')
        else:
            break

    for i in range(qtd):
        name = input(f'Nome do 1°{i+1} TANQUE: ')
        tanks[chr(65 + i)] = Tank(name)

    return tanks


def main():
    print(f'{"*" * 25} Batalha de Tanques {"*" * 25}\n')
    print(f'{"_" * 18} Cada jogador deve criar um tanque !{"_" * 18}\n')

    tanks = create_tank()
    players = list(tanks.keys())

    def player_info():
        for player in players:
            print(tanks[player])

    while len(tanks) != 1:
        random.shuffle(players)

        for current_player in players:
            enemy_players = [player for player in tanks if player != current_player]

            print(f"{tanks[current_player]} fará um ataque!\n")

            for i, enemy in enumerate(enemy_players):
                print(f'{i + 1}: {tanks[enemy]}')

            while True:
                try:
                    choice = int(input(f'{current_player}, escolha o alvo (1-{len(enemy_players)}): '))
                    if 1 <= choice <= len(enemy_players):
                        break
                    else:
                        print("Escolha inválida! Digite um número entre 1 e", len(enemy_players))
                except ValueError:
                    print("Escolha inválida! Digite um número entre 1 e", len(enemy_players))

            target = enemy_players[choice - 1]

            print(f"{tanks[current_player]} ATACA {tanks[target]}")
            tanks[current_player].fire_at(tanks[target])
            print(f'{"-" * 70}\n')

            if not tanks[target].alive: 
                print(f" {tanks[target]} fora do jogo!")
                tanks.pop(target)
                print(f'{"-" * 70}\n')
        
        player_info()
    
    print(f"VENCEDOR: {tanks[list(tanks.keys())[0]]}")

if __name__ == "__main__":
    main()
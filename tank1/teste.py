import random

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 50
        self.armor = 60

    def __str__(self):
        if self.alive:
            return "%s (%i armadura, %i munições)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DESTRUIDO)" % self.name

    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, "dispara em", enemy.name)
            enemy.hit()
        else:
            print(self.name, "não tem munição!")

    def hit(self):
        self.armor -= 20
        print(self.name, "foi atingido")
        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "foi destruído!")


def create_tank():
    tanks = {}
    while True:
        qtd = int(input('Quantos tanques vão jogar?[2/10]: '))
        if qtd < 2 or qtd > 10:
            print('Quantidade inválida!! Digite de 2 a 10 jogadores!')
        else:
            break

    for i in range(qtd):
        name = input(f'Nome do {i+1}° TANQUE: ')
        tanks[chr(65 + i)] = Tank(name)

    return tanks


def main():
    print(f'{"*" * 25} Batalha de Tanques {"*" * 25}\n')
    print(f'{"_" * 18} Cada jogador deve criar um tanque! {"_" * 18}\n')

    tanks = create_tank()
    players = list(tanks.keys())

    def player_info():
        for player in players:
            print(tanks[player])

    while len(tanks) != 1:
        random.shuffle(players)

        for current_player in players:
            if not tanks[current_player].alive:
                continue

            enemy_players = {k: tanks[k] for k in tanks if k != current_player and tanks[k].alive}

            print(f"{tanks[current_player]} fará um ataque!\n")

            for key, enemy in enemy_players.items():
                print(f"{key}: {enemy}")

            while True:
                target_key = input(f'{tanks[current_player].name}, escolha o alvo ({" ".join(enemy_players.keys())}): ').upper()
                if target_key in enemy_players:
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

        player_info()

    print(f"VENCEDOR: {tanks[list(tanks.keys())[0]]}")

if __name__ == "__main__":
    main()
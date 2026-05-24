import random

class Hero:

    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        self.death = False

    def take_damage(self, amount: int):
        damage = random.randint(1,amount)
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        print(f'{self.name} получил {damage}! Его здоровье: {self.hp}')
    
    def fight(self, enemy: str):
        self.enemy = Hero(enemy, 100)
        print(f'Началась битва! {enemy} v.s {self.name}')
        while self.enemy.hp > 0 and self.hp > 0:

            print(f'Бьет {enemy}!')
            self.take_damage(30)

            if self.hp <= 0:
               print(f'{self.name} мертв! {enemy} выиграл битву. Вы проиграли.')
               self.death = True
               break

            print(f'Бьет {self.name}!')
            self.enemy.take_damage(30)

            if self.enemy.hp <= 0:
                print(f'{enemy} мертв! {self.name} выиграл битву. ')
                break

    def rest(self, time: int):
        if self.death:
            return
        elif time > 30:
            time = 30
        else:
            self.hp += (time * 0.5)
            print(f'{self.name} отдохнул. Он получил {time * 0.5} урона. Его хп: {self.hp}')
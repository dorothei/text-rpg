import random

# герои

class Character:

    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        self.death = False

    def take_random_damage(self, amount):
        damage = random.randint(1, amount)
        self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
            self.death = True
        print(f'{self.name}: -{damage}! HP: {self.hp}')

    def take_fixed_damage(self, value):
        self.hp -= value

        if self.hp <= 0:
            self.hp = 0
            self.death = True
        print(f'{self.name}:  -{value}! HP: {self.hp}')

    def rest(self):
        if self.death:
            return
        self.hp += (self.hp // 10)
        print(f'{self.name} отдохнул. Его хп: {self.hp}')

class Main(Character):

    def superpunch(self, target):
        chance = random.randint(0,3)
        if chance != 3:
            print(f'СУПЕР-УДАР! {self.name} сделал супер удар.')
            target.take_fixed_damage(50)
        else:
            print(f'МИМО! {self.name} легонько коснулся врага.')
            target.take_fixed_damage(20)

# враги

class CommonEnemy(Character):

    def __init__(self, hp: int):
        randomname = random.choice(['Кровопряд', 'Ржавочервь', 'Грёзостраж', 'Пеплород'])
        super().__init__(randomname, hp)


    def poison(self, target):
        chance = random.randint(1,4)
        if chance == 1:
            print(f'Монстр впрыснул яд!')
            target.take_random_damage(20)
            target.take_fixed_damage(10)
        else:
            target.take_random_damage(15)

class Boss(Character):

    def __init__(self, name: str, hp: int):
        super().__init__(name, hp)
        self.qte = False

    def reversedamage(self, target):
        chance = random.randint(1,3)
        if chance == 1:
            print('ШИПЫ! Босс отразил удар.')
    
    def dotdamage(self, target):
        chance = random.randint(1,3)
        if chance == 1:
            print('🥀 Дева Розы раскрыла ядовитые шипы!')
            for i in range(1,10):
                if target.death:
                    break
                target.take_fixed_damage(2)

        elif self.qte is False and chance == 3:
            count = 1
            vs = 0
            while vs != 3 and count != 5:
                randomcte = random.randint(1,10)
                print(f'🥀 Стебли роз душат вас! Попытки: {count}/5')
                print(f'{randomcte} - Вырываться')
                print("========================")
                ctechoice = input('')

                if ctechoice == str(randomcte):
                    vs += 1
                    print(f'🥀 Вы рвете стебли! Стеблей порвано: {vs}/3 ')
                    print("========================")
                    self.take_fixed_damage(10)
                    count += 1

                else:
                    print('🥀 Роза душит еще сильнее!')
                    print("========================")
                    target.take_fixed_damage(10)
                    count += 1

            if vs != 3:
                    target.death = True
                    print('💀 Вы были задушены стеблями Девы Роз.')
                    
            else:
                print('🥀 Вы выбрались из оков роз! Бой продолжается.')
                self.qte = True
        else:
            print('🥀 Острые как бритва лепестки закружились в воздухе, рассекая вашу кожу!')
            print("========================")
            target.take_fixed_damage(20)




# тех

class Fight:

    def fight(self, mainguy: Main, enemy: CommonEnemy):
        
        print(f'Началась битва! {enemy.name} v.s {mainguy.name}')
        while not mainguy.death and not enemy.death:
            print('Что делать?')
            print('1 - Нападать!')
            print('2 - Отдых')
            choice = int(input(''))
            
            if choice == 1:
                mainguy.superpunch(enemy)
                if enemy.death:
                    break
            elif choice == 2:
                mainguy.rest()
            else:
                print('Такого действия нет!')
                continue

            # ход врага
            randchoice = random.randint(1,4)    
            if randchoice == 4:
                enemy.rest()
            else:
                print(f'Бьет {enemy.name}!')
                enemy.poison(mainguy)

        print("========================")
        if mainguy.death:
           print(f'{mainguy.name} мертв! {enemy.name} выиграл битву. Вы проиграли.')
           print('Конец игры.')

        if enemy.death:
            print(f'{enemy.name} мертв! {mainguy.name} выиграл битву. ')
        print("========================")

class RoseBossFight:

    def bossfight(self, mainguy: Main, boss: Boss):
        print(f'🥀 Дева Роз атакует первой, застав {mainguy.name} в расплох.')
        print(f'🥀 БОСС! {boss.name} v.s {mainguy.name}')
        while not mainguy.death and not boss.death:

            print('Ход Девы Роз!')
            if boss.hp <= 100:
                chance = random.randint(1,2)
                if chance == 1:
                    boss.rest()
                else:
                    boss.dotdamage(mainguy)
                    if mainguy.death:
                        break
            else:
                boss.dotdamage(mainguy)
                if mainguy.death:
                    break

            print("========================")

            print('Что делать?')
            print('1 - Нападать!')
            print('2 - Отдых')
            choice = int(input(''))

            if choice == 1:
                mainguy.superpunch(boss)
                if boss.death:
                    break
            elif choice == 2:
                mainguy.rest()
            else:
                print('Такого действия нет!')
                continue

            print("========================")


        if mainguy.death:
                print(f'{mainguy.name} мертв! {boss.name} выиграла битву. Вы проиграли.')
                print('Конец игры.')
                
        if boss.death:
            print(f'{boss.name} мертва! {mainguy.name} выиграл битву. ')
            print("========================")

class Game:

    def __init__(self):
        print('⚔️  Добро пожаловать в TEST RPG! ⚔️')
        print("========================")
        player_name = input("Введите имя вашего героя: ")
        self.player = Main(player_name, 100)
        print('Вы идете вперед по темному лесу.')
        print('На пути развилка. Куда вы пойдете?')
        print('1 - Направо')
        print('2 - Налево')
        first = input('')

        if first == '1':
            print('Вы пошли направо.')
            print('Вы встретили сундук около дерева.')
            print('Открыть его?')
            print('1 - Да')
            input('')
            print('Из сундука несёт кровью...')
            input('')
            Fight().fight(self.player, CommonEnemy(100))
        
        elif first == '2':
            print('Вы пришли на поле, полностью усеянное красными цветущими розами.')
            print('В цветах что-то блестит.')
            print('Посмотреть?')
            print('1 - Да.')
            input('')
            print('Вы чувствуете, как в ваши ноги впиваются шипы роз...')
            input('')
            RoseBossFight().bossfight(self.player, Boss('Дева Розы', 200))


Game()
####
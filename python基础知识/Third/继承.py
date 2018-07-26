class Hero:

    def __init__(self,nickname,life_value,aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attck(self, enemy):
        enemy.life_value -= self.aggresivity

class PA(Hero):
    camp = 'tianhui'
    def attck(self, enemy):
        Hero.attck(self,enemy)  #指名道姓
        enemy.life_value -= self.aggresivity


class TA(Hero):
    camp = 'yeyan'







class PA:
    camp = 'tianhui'
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity
    def attck(self,enemy):
        enemy.life_value -= self.aggresivity

class TA:
    camp = 'yeyan'
    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity
    def attck(self, enemy):
        enemy.life_value -= self.aggresivity

p1 = PA('chuhan',100,30)
t1 = TA('chenhw',80,50)


print(t1.life_value)
p1.attck(t1)
print(t1.life_value)
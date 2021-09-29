class Human():
    def __init__(self,power,health,stamina):
        self.power=power
        self.health=health
        self.stamina=stamina
    def go2work (self):
        print('я еду на завод')
    def work (self):
        print('я работаю')
    def eat (self):
        print('я ем')
    def info (self):
        print('Сила = ',self.power,"\r\n",'Здоровье = ',self.health,"\r\n",'Выносливость' ,self.stamina)
whitepower=Human(100,150,100)
blackpower=Human(150,100,90)
print('Белый:',"\r\n",whitepower.power,whitepower.health,whitepower.stamina)
print('черный:',"\r\n",blackpower.power,blackpower.health,blackpower.stamina)
whitepower.info()
blackpower.info()
l=0
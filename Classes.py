class Car():
    def __init__(self,power,type,model):
        self.power=power
        self.type=type
        self.model=model
    def go (self):
        print('я еду вперед')
    def left (self):
        print('я еду влево')
    def right (self):
        print('я еду вправо')
    def info (self):
        print(self.type,self.model,self.power)
civic1=Car(80,'hatch','civic')
civic2=Car(325,'hothatch','civic type R')
print(civic1.model)
print(civic1.type)
print(civic1.power)
print(civic2.model)
print(civic2.type)
print(civic2.power)
civic1.go()
civic2.left()
civic1.right()
civic2.info()


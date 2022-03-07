import turtle
import random

window=turtle.Screen()
window.bgcolor('black')

class Enemy(object):
    element=turtle.Turtle()
    position=[]
    def __init__(self,element,position):
        self.element=element
        self.position=position
    def begin(self):
        self.element.penup()
        self.element.shape('arrow')
        self.element.color('green')
        self.element.goto(self.position[0],self.position[1])




enemy=[]
for i in range(3):
    mhor=random.randint(-300,300)
    mver=random.randint(-300,300)
    newEnemy=Enemy(turtle.Turtle(),[(mhor),(mver)])
    newEnemy.begin()
    enemy.append(newEnemy)

enemy=Enemy(turtle.Turtle(),[0,0])
enemy.begin()

window.mainloop()
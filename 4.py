import random
import turtle
import time

colors=["light green","aqua","pink","orange","yellow"]
class Fractals:
    def __init__(self):
        pass
        
        
    def draw(self):
        repeatition=int(input("How many time?"))
        length=int(input("Enter the length:"))
        sides=int(input("How many sides?"))
        t=turtle.Pen()
        for j in range(repeatition):
            for i in range(sides):
                turtle.Screen().bgcolor("black")
                t.speed(10000)
                t.pencolor(random.choice(colors))
                t.forward(length)
                t.lt(360/sides)
            t.lt(10)
       
   
fractal=Fractals()
t1=time.time()
fractal.draw()
t2=time.time()
print("Performance Time is %s second:"%(round(t2-t1,2)))

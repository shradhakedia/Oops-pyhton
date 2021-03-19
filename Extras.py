'''
list1=[7,6,4,3,9,3,2]
l=list1.copy()
l.remove(max(l))
print(max(l))


#function returning a function...decorater starts here
def create_adder(x):  
    def adder(y):  
        return x+y  
  
    return adder  
  
add_15 = create_adder(15)  
  
print(add_15(10))
'''
'''
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

#square
from turtle import *
for i in range(4):
    forward(200)
    right(90)

#star
import turtle
obj = turtle.Turtle()

for i in range(5):
    obj.forward(100)
    obj.right(144)
'''
import turtle
turtle.color('blue')
style = ('Courier', 90, 'normal')
turtle.write('SHRADHA', font=style, align='center')
turtle.hideturtle()	
turtle.done()
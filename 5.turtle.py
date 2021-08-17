import turtle

colors=['red','purple','blue','green','yellow','orange']

turtle.bgcolor('black')

aydin= turtle.Turtle()
f= int(input("Please enter your shapes yo want:"))
p=3
k= 50
aydin.pencolor('green')
pos1=0
pos2=0

while p<= f:
    for i in range(p):
        aydin.forward(k)
        aydin.left(360/p)
    p+=1
    k+=10
    pos1-=10
    pos2 -= 10
    aydin.penup()
    aydin.goto(pos1,pos2)
    aydin.pendown()




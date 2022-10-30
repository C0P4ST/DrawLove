import turtle 

t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("black")

#gambar love
t.color("red")
t.fillcolor("red")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)

t.end_fill()

#writing
t.up()
t.setpos(-110,150)
t.down()
t.color("white")
t.write("I LOVE YOU", font =("Rockwell Nova", 8, "bold"))

#writing2
t.up()
t.setpos(-55,100)
t.color("Black")
t.write("TAPI BO'ONG",font=("Rockwell Nova",3, "bold"))

t.ht()
turtle.mainloop()
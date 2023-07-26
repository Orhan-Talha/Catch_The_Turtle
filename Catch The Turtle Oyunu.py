import turtle
s=turtle.Screen()
s.bgcolor("lightblue")
s.title("Catch The Turtle")
sc=0
score="score = {}"
txt = turtle.Turtle()
txt.color("blue")
txt.penup()
txt.ht()
top_height = s.window_height()/2  # positive height/2 is the top of the screen
y = top_height - top_height/10  # decreasing a little bit so text will be visible
txt.setposition(0, y)
txt.write(arg=score.format(sc), move=True, align='center', font=("arial", 20, "normal"))
turtle1 = turtle.Turtle()
turtle1.shapesize(stretch_wid=2, stretch_len=2, outline=None)
turtle1.shape("turtle")
turtle1.color("green")
turtle1.penup()





















turtle.mainloop()















































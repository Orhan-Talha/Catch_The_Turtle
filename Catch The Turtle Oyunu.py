import turtle
s=turtle.Screen()
s.bgcolor("lightblue")
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
























turtle.done()















































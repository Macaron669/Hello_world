""" Test sur turtle """

import turtle

turtle.up()
turtle.goto(-150,-150)
turtle.down()
turtle.color("pink")
turtle.begin_fill()
turtle.goto(150,-150)
turtle.goto(150,150)
turtle.goto(-150,150)
turtle.goto(-150,-150)
turtle.end_fill()
turtle.done() # turtle.mainloop()

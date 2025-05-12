import turtle
class TurtleForNoobs:
    def cuadrado(self):
        skk = turtle.Turtle()
        for i in range (4):
            skk.forward(50)
            skk.right(90)
        turtle.done()


    def estrella(self):
        star = turtle.Turtle()
        for i in range(40):
            star.right(10)
            star.forward(25)
            star.right(10)
            star.forward(25)
            star.right(10)
            star.forward(25)
            star.right(10)
            star.forward(25)
        turtle.done()

    def ks(self, length, d):
        if d == 0:
            turtle.forward(length)
        else:
            length = length / 3
            d = d - 1
            self.ks(length, d)
            turtle.right(60)
            self.ks(length, d)
            turtle.ks(120)
            self.ks(length, d)
            turtle.right(60)
            self.ks(length, d)

    def snowflake(self):
        turtle.reset()
        turtle.ht()
        colors = ["green", "purple", "white" ]
        for i in range(3):
            turtle.color(colors[i])
            self.ks(200, 3)
            turtle.left(120)
        turtle.update()
        turtle.done()
        
t = TurtleForNoobs()
t.snowflake()
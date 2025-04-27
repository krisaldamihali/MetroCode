from manim import *


class myscene(Scene):
    def construct(self):
        circle = Square()  # create a circle
        # circle.set_fill(PINK, opacity=1)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        self.wait(1)
        self.play(circle.animate.set_fill(BLUE, opacity=1))

        fjalia = Text("Hello World")
        self.play(Write(fjalia))
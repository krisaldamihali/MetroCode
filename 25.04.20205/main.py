from manim import *


class myscene(Scene):
    def construct(self):
        square = Square()  # create a square
        # square.set_fill(PINK, opacity=1)  # set the color and transparency
        self.play(Create(square))  # show the square on screen
        self.wait(1)
        self.play(square.animate.set_fill(BLUE, opacity=1))
        self.wait(1)
        self.play(Write(Text("Ky eshte nje katror", font_size=100, color=RED, fill_opacity=1, font="Arial")))
        self.wait(4)

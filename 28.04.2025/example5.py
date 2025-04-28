from manim import *

class RotatingSquare(Scene):
    def construct(self):
        square = Square(color=PURPLE).scale(1.5)
        self.play(Create(square))
        self.play(Rotate(square, angle=PI/2))
        self.wait(2)

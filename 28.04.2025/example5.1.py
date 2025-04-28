from manim import *

class RotatingTriangle(Scene):
    def construct(self):
        # Krijo trekëndëshin
        triangle = Polygon(ORIGIN, RIGHT * 2, UP * 2, color=BLUE)
        triangle.set_fill(BLUE, opacity=0.5)
        
        # Animo krijimin
        self.play(Create(triangle))
        self.wait(1)
        
        # Animo rrotullimin e trekëndëshit për 90 gradë (PI/2 radian)
        self.play(Rotate(triangle, angle=PI/2))
        self.wait(2)

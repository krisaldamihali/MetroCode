from manim import *

class TriangleExample(Scene):
    def construct(self):
        triangle = Polygon(ORIGIN, RIGHT, UP, color=BLUE)
        triangle.set_fill(BLUE, opacity=0.5)
        
        self.play(Create(triangle))
        self.wait(1)

        labels = VGroup(
            MathTex("A").next_to(ORIGIN, DOWN+LEFT),
            MathTex("B").next_to(RIGHT, DOWN+RIGHT),
            MathTex("C").next_to(UP, UP+LEFT),
        )
        
        self.play(Write(labels))
        self.wait(2)

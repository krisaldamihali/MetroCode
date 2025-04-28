from manim import *

class TrianglePerimeter(Scene):
    def construct(self):
        triangle = Polygon(ORIGIN, RIGHT*3, UP*2, color=BLUE)
        triangle.set_fill(BLUE, opacity=0.4)
        
        perimeter_formula = MathTex("P = a + b + c").to_edge(UP)

        self.play(Create(triangle))
        self.wait(1)
        self.play(Write(perimeter_formula))
        self.wait(2)

from manim import *

class RectangleFormulas(Scene):
    def construct(self):
        rectangle = Rectangle(width=4, height=2, color=ORANGE)
        rectangle.set_fill(ORANGE, opacity=0.5)

        area_formula = MathTex("A = l \\times w").to_corner(UL)
        perimeter_formula = MathTex("P = 2(l + w)").to_corner(UR)

        self.play(Create(rectangle))
        self.wait(1)
        self.play(Write(area_formula), Write(perimeter_formula))
        self.wait(2)

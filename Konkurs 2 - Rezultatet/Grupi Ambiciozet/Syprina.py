from manim import *


class RectangleFormulas(Scene):
    def construct(self):
        rectangle = Rectangle(width=4, height=2, color=ORANGE)
        rectangle.set_fill(ORANGE, opacity=0.5)
        area_formulas = MathTex("S = 16 \\times 2").to_corner(UL)
        syprina_formula = MathTex("S = a * b").to_corner(UR)
       
        self.play(Create(rectangle))
        self.wait(1)
        self.play(Write(area_formulas), Write(syprina_formula))
        self.wait(2)
        def construct(self):
        square = Square(width=4, height=2, color=ORANGE)
        square.set_fill(ORANGE, opacity=0.5)
       
        area_formulas = MathTex("S = 16 \\times 2").to_corner(UL)
        syprina_formula = MathTex("S = a**2").to_corner(UR)

        self.play(Create(square))
        self.wait(1)
        self.play(Write(area_formula), Write(syprina_formula))
        self.wait(2)

class CircleFormulas(Scene):
    def construct(self):
        circle = Circle(width=4, height=2, color=ORANGE)
        circle.set_fill(ORANGE, opacity=0.5)
                
        area_formulas = MathTex("S = 16 \\times 2").to_corner(UL)
        syprina_formula = MathTex("S = PI r**2").to_corner(UR)
        self.play(Create(circle))
        self.wait(1)
        self.play(Write(area_formula), Write(syprina_formula))
        self.wait(2)
        
 
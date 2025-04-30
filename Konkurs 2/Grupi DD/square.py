from manim import *

class SquareSiperfaqa(Scene):
    def construct(self):
        square = Square(color=GREEN).shift(RIGHT*3 + UP*2)
        square.set_fill(GREEN, opacity=1)

        siperfaqa_formula = MathTex(r"S=a^2").shift(RIGHT*3 + UP*2)

        self.play(Create(square))
        self.wait(1.0)
        self.play(Write(siperfaqa_formula))
        self.wait(2.0)

        circle = Circle(color=RED).shift(LEFT*3 + DOWN*2)
        circle.set_fill(RED, opacity=1)

        siperfaqa_formula = MathTex(r"S=\pi r^2").shift(LEFT*3 + DOWN*2)

        self.play(Create(circle))
        self.wait(1)
        self.play(Write(siperfaqa_formula))
        self.wait(2)

        triangle = Triangle(color=BLUE)
        triangle.set_fill(BLUE, opacity=1)
        
        siperfaqa_formula = MathTex(r"s = b + h/2")

        self.play(Create(triangle))
        self.wait(1)
        self.play(Write(siperfaqa_formula))
        self.wait(2)

        



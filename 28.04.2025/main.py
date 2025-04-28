from manim import *

class FormulaExample(Scene):
    def construct(self):
        formula = MathTex("e^{i\\pi} + 1 = 0")
        formula.set_color_by_gradient(BLUE, GREEN)
        self.play(Write(formula))
        self.wait(2)
        self.play(formula.animate.scale(2))
        self.wait(1)
        self.play(FadeOut(formula))

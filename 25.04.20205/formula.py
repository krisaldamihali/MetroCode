from manim import *


class animateFormula(Scene):
    def construct(self):
        formula = Tex(r"\sqrt{5}")
        self.play(Write(formula))
        
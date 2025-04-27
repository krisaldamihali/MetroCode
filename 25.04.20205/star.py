from manim import *

class myscene(Scene):
    def construct(self):
        star = Star(inner_radius=3)
        self.play(Create(star))
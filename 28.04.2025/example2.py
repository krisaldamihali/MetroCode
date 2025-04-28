from manim import *

class VectorExample(Scene):
    def construct(self):
        vec = Arrow(ORIGIN, RIGHT * 2 + UP, buff=0)
        label = MathTex("\\vec{v}").next_to(vec.get_end(), RIGHT)

        self.play(GrowArrow(vec), Write(label))
        self.wait(1)

        self.play(vec.animate.shift(LEFT*2 + DOWN), label.animate.shift(LEFT*2 + DOWN))
        self.wait(2)

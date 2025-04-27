from manim import *

class animateText(Scene):
    def construct(self):
        text = Text("Yjet e MetroCode",
         font_size=96)
        self.play(Write(text))
        self.wait(4)
        
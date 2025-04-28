from manim import *

class CircleWithLabel(Scene):
    def construct(self):
        circle = Circle(radius=2, color=GREEN)
        circle.set_fill(GREEN, opacity=0.3)
        label = Text("Qarku", font_size=48)
        
        self.play(Create(circle))
        self.play(Write(label))
        self.play(label.animate.move_to(circle.get_center()))
        self.wait(2)

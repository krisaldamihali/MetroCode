from re import X
from tkinter import Y
from manim import*
class linearfunction(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],  # x nga -3 deri 3
            y_range=[-10, 10, 1],  # y nga -10 deri 10
            axis_config={"color": WHITE}
        )
        linear_graph = axes.plot(lambda x: 2*x+2, color=YELLOW)
        label = axes.get_graph_label(linear_graph, label="y=2x+2")
        self.play(Create(axes))
        self.play(Create(linear_graph), Write(label))
        self.wait(2)
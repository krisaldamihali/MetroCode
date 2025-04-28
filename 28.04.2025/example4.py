from manim import *

class ParabolaPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-1, 9],
            axis_config={"color": BLUE},
        )
        parabola = axes.plot(lambda x: x**2, color=RED)
        label = axes.get_graph_label(parabola, label="y=x^2")

        self.play(Create(axes), Create(parabola), Write(label))
        self.wait(2)

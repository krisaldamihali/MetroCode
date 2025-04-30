from manim import *
class GraphicLine(Scene):
    def construct(self):
        axes= Axes(
            x_range =[-5,5],
            y_range =[-10,10],
        )

        m=ValueTracker(1)
        c=ValueTracker(0)
   

        graph=axes.plot(lambda x : m.get_value() * x + c.get_value(), color=WHITE)
        graph_label=axes.get_graph_label( graph, label ="y = mx + c")

        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(1.0)

        self.play(m.animate.set_value(2),c.animate.set_value(1), run_time=3)
        self.wait(1.0)

        self.play(m.animate.set_value(-1), c.animate.set_value(-2), run_time = 3)
        self.wait(2.0)
        
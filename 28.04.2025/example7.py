from manim import *

class CubeFunctionPlot(Scene):
    def construct(self):
        # Krijo aksat
        axes = Axes(
            x_range=[-3, 3, 1],  # x nga -3 deri 3
            y_range=[-10, 10, 2],  # y nga -10 deri 10
            axis_config={"color": WHITE}
        )

        # Krijo grafikun y = x^3
        cube_graph = axes.plot(lambda x: x**3, color=YELLOW)
        
        # Shto etiketën e funksionit
        label = axes.get_graph_label(cube_graph, label="y = x^3")
        
        # Animacionet
        self.play(Create(axes))
        self.play(Create(cube_graph), Write(label))
        self.wait(2)

        # Një pikë që lëviz mbi grafikun
        dot = Dot(color=RED).move_to(axes.c2p(1, 1))
        self.play(FadeIn(dot))

        # Animo dot-in duke ndjekur grafikun
        self.play(
            MoveAlongPath(dot, cube_graph),
            run_time=5,
            rate_func=linear
        )
        
        self.wait(2)

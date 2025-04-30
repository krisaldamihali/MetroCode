from manim import *

class LinearSystemGraph(Scene):
    def construct(self):  #sistemi-  y= 2x+1, y= -x +4
        axes = Axes(
            x_range=[-4, 4, 1],  
            y_range=[-5, 5, 1],  
            axis_config={"color": WHITE}
        )
        linear_graph = axes.plot(lambda x: 2*x+1, color=RED)
        label = axes.get_graph_label(linear_graph, label="y = 2x+1")
        self.play(Create(axes))
        self.play(Create(linear_graph), Write(label))
        self.wait(2)
        
        linear_graph = axes.plot(lambda x: -x+4, color=GREEN)
        label = axes.get_graph_label(linear_graph, label="y = -x+4")
        self.play(Create(axes))
        self.play(Create(linear_graph), Write(label))
        
        dot = Dot(color=YELLOW)
       
        self.play(FadeIn(dot))
        
        self.play(
            Create(linear_graph),
            Create(dot), 
            run_time=5,
            rate_func=linear
        )
        
        self.wait(2)



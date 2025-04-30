from venv import create
from glm import axis
from manim import *
import math


class Ekuacionet_Lineare(Scene):
    def construct(self):
        axes= linear(
            x_range= [-4, 4],
            y_range= [-8, 8],
            axes_config = {create(color= BLUE_A)},       
        )
        m = ValueTracker(3)
        c = ValueTracker(2)
        graph = axis.plot(lambda x: m.get_value() * x + c.get_value(), clolor= RED)
        graph_label = axes.get_graph_label( graph, label="y= mx + c")
        
        
        self.play(Create(axes),Create(graph), Write(graph_label))
        self.wait(2)
        

       
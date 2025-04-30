from manim import *
#Zgjidhja grafike e një sistemi ekuacionesh lineare. Animo dy
# drejtëza dhe pikëprerjen e tyre që është zgjidhja e sistemit
#Write(text), Create(linear), Create(linear1), Write(label),
                   #Write(label1), FadeIn(zgjidhja))
class LinearPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 5],
            y_range=[-3, 5],
            axis_config={"color": WHITE},
        )
        linear= axes.plot(lambda x: x, color= RED)
        linear1= axes.plot(lambda x: -x+1, color= BLUE)
        label = axes.get_graph_label(linear, label="y=x")
        label1 = axes.get_graph_label(linear1, label="y=-x+1")
        zgjidhja= Dot(color= GREEN).move_to(axes.c2p(0.5, 0.5))

        text=Text("zgjidhja", font_size=15).next_to(zgjidhja, RIGHT)
        
        
       
        self.play(Create(axes))
        self.wait()
        self.play(Create(linear))
        self.play(Write(label))
        self.wait()
        self.play(Create(linear1))
        self.play(Write(label1))
        self.wait()
        self.play(FadeIn(zgjidhja))
        self.play(FadeIn(text))
        self.wait(3)
       
       

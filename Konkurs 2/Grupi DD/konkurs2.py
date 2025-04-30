from manim import *



class FunksioniLinear(Scene):
    def construct(self):   
        axes = Axes(
            x_range=[-5,5],
            y_range=[-5,5],
            axis_config={"color": YELLOW}
        )
        linear = axes.plot(lambda x :x,color=BLUE)
        self.play(Create(linear))
        self.wait(7.0)
        
        
        text1 = Text("y = mx + c",font_size=15).to_corner(UL+ DOWN*2)
        text2 = Text("c eshte pikeprerja me boshtin  e y",font_size=15).to_corner(UL+DOWN*3)
        text3 = Text("m eshte koeficenti i drejtezes",font_size=15).to_corner(UL,DOWN*4)
        text4 = Text("c",font_size=15).next_to(ORIGIN+RIGHT)
        self.play(Create(axes))
        self.play(Write(text1),Write(text2),Write(text3),Write(text4))
        self.wait(5.0)

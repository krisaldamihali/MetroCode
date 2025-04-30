from manim import *

class TriangleExample(Scene):
    def construct(self):
        triangle = Polygon(ORIGIN, RIGHT, UP, color=BLUE)
        triangle.set_fill(RED, opacity=0.5)
        
        self.play(Create(triangle))
        self.wait(1)

        perimeter_formula = MathTex("P = a + b + c").to_edge(UP)

        labels = VGroup(
            MathTex("a").next_to(triangle, DOWN),
            MathTex("b").next_to(triangle, LEFT),
            MathTex("h").next_to(triangle.get_edge_center(RIGHT*0.5), UP*0.5),


        )
        
        self.play(Write(labels))
        self.wait(2)

        
        recta = Rectangle(width=1.0, height=1.0).next_to(ORIGIN, (DOWN*0.18)+(RIGHT*0.15))
        rectb = Rectangle(width=1.0, height=1.0).next_to(ORIGIN, (UP*0.18)+(LEFT*0.15))
        rectc = Rectangle(width=1.5, height=1.5).next_to(ORIGIN, (UP*1)+(RIGHT*1))
        rectc.rotate(PI/4)
        

        self.play(Create(recta))
        self.play(Create(rectb))
        self.play(Create(rectc))
        self.wait(1.0)
        
        label2 = VGroup(
            MathTex("h^2=a^2+b^2").next_to(triangle, UP*6),

        )
        
        self.play(Write(label2))
        self.wait(2)

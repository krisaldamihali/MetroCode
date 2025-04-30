from manim import*
class RectangleArea(Scene):
    def construction(self):
        drejtekendesh=Rectangle(Width=2 , Height=3)
        drejtekendesh.set_fill(color=RED, opacity=0.5)
        area_formula=MathTex("A=W*H")
        self.play(Create(drejtekendesh))
        self.wait(2.3)
        self.play(Write(area_formula))
        self.wait(2.3)

        katror=Square(side=2)
        katror.set_fill(color=RED, opacity=1)
        area_formula=MathTex(side**2)
        self.play(Create(katror))
        self.wait(2)
        self.play(Write(katror))
        self.wait(2.3)


        rreth=Circle(radius=3)
        rreth.set_fill(color=RED, opacity=1)
        area_formula=MathTex(side**2)
        self.play(Create(rreth))
        self.wait(2)
        self.play(Write(area_formula))
        self.wait(2.3)

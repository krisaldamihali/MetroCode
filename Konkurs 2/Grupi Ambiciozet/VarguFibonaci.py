from manim import*
class VarguFib(Scene):
    def construct(self):
       vargu=[0,1]
for_ in range(8): vargu.append(vargu[-1]+vargu[-2])
self.play(Write(Text(str)))
self.wait(2)

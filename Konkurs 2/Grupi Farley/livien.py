from manim import *

class FibonacciSequence(Scene):
    def construct(self):
        title = Text("Fibonacci Sequence").scale(1.5)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        formula = MathTex(r"F_n = F_{n-1} + F_{n-2}")
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(formula))

        fib_sequence = [0, 1]
        for _ in range(8):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

        number_mobs = [Text(str(n), font_size=48) for n in fib_sequence]
        sequence_group = VGroup(*number_mobs).arrange(RIGHT, buff=0.5).to_edge(DOWN)

        self.play(Write(sequence_group))
        self.wait(1)
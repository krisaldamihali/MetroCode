from manim import *

class PythagorasTheorem(Scene):
    def construct(self):
        # Create a right triangle
        triangle = Polygon(
            LEFT, RIGHT, UP, color=BLUE, fill_opacity=0.5
        ).shift(2 * LEFT)

        # Label the sides
        a_label = MathTex("a").next_to(triangle.get_left(), DOWN)
        b_label = MathTex("b").next_to(triangle.get_top(), LEFT)
        c_label = MathTex("c").next_to(triangle.get_right(), RIGHT)

        # Label for the Pythagorean Theorem
        theorem_text = MathTex("a^2 + b^2 = c^2").to_edge(UP)

        # Create squares on each side
        square_a = Square(side_length=3, color=BLUE, fill_opacity=0.3).shift(2 * LEFT)
        square_b = Square(side_length=2, color=GREEN, fill_opacity=0.3).shift(UP + 2 * LEFT)
        square_c = Square(side_length=5, color=RED, fill_opacity=0.3).shift(RIGHT + 1 * UP)

        # Add all elements to the scene
        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.play(Write(theorem_text))
        
        # Display the squares
        self.play(Create(square_a), Create(square_b), Create(square_c))
        self.wait(1)

        # Animate showing the Pythagorean Theorem
        self.play(Write(theorem_text))
        self.wait(2)

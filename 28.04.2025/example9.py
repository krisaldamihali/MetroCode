from manim import *
import random

class WelcomeStarsWithShapes(Scene):
    def construct(self):
        # Krijo tekstin
        welcome_text = Text(
            "Mirë se erdhët yje!",
            font_size=72,
            color=YELLOW
        )
        welcome_text.set_z_index(2)  # Që të jetë mbi yjet

        # Shtojmë shumë yje me forma të vërteta
        stars = VGroup()
        for _ in range(50):  # 50 yje
            x = random.uniform(-7, 7)
            y = random.uniform(-4, 4)

            # Krijojmë një formë ylli me 5 pika
            star = Polygon(
                *[np.array([np.cos(2 * np.pi * i / 5), np.sin(2 * np.pi * i / 5), 0]) for i in range(5)],
                color=WHITE
            )
            star.set_fill(WHITE, opacity=0.8)
            star.move_to([x, y, 0])
            star.set_z_index(1)
            stars.add(star)

        # Animacioni i yjeve (shfaqje graduale)
        self.play(
            LaggedStartMap(FadeIn, stars, lag_ratio=0.05),
            run_time=3
        )

        # Animacioni i tekstit
        self.play(Write(welcome_text))
        self.wait(2)

        # Efekt i lehtë lëvizje për yjet
        self.play(
            stars.animate.shift(DOWN * 0.5),
            run_time=3,
            rate_func=there_and_back
        )

        self.wait(2)

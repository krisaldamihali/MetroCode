from manim import * 
import random
import numpy as np

class WelcomeStarsEpic(Scene):
    def create_star(self, radius=0.2, color=YELLOW):
        points = []
        for i in range(10):
            angle = np.pi / 5 * i
            r = radius if i % 2 == 0 else radius * 0.4
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            points.append([x, y, 0])
        star = Polygon(*points, color=color).set_fill(color, opacity=1)
        return star

    def create_sun_rays(self, radius=2.8, ray_length=1.0, num_rays=20, color=YELLOW):
        rays = VGroup()
        for i in range(num_rays):
            angle = 2 * PI / num_rays * i
            start = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            end = np.array([(radius + ray_length) * np.cos(angle), (radius + ray_length) * np.sin(angle), 0])
            ray = Line(start, end, stroke_color=color, stroke_width=4, stroke_opacity=0.6)
            rays.add(ray)
        return rays

    def construct(self):
        # Sfond blu qielli
        self.camera.background_color = "#001f3f"  # blu e errët (natë)

        sun_radius = 2.8
        safe_zone_radius = sun_radius + 0.3  # Yjet nuk lejohen brenda këtij rreze

        # Yjet - jashtë zonës së diellit
        stars = VGroup()
        while len(stars) < 60:
            x = random.uniform(-7, 7)
            y = random.uniform(-4, 4)
            pos = np.array([x, y, 0])
            if np.linalg.norm(pos) < safe_zone_radius:
                continue
            star = self.create_star(radius=random.uniform(0.15, 0.25))
            star.move_to(pos).set_z_index(1)
            stars.add(star)

        self.play(LaggedStartMap(FadeIn, stars, lag_ratio=0.03), run_time=3)

        # Dielli - rreth dhe rreze
        glow_circle = Circle(radius=sun_radius, color=YELLOW, fill_opacity=0.2)
        glow_circle.set_z_index(2)
        glow_circle.move_to(ORIGIN)

        sun_rays = self.create_sun_rays(radius=sun_radius, ray_length=1.0, num_rays=20, color=YELLOW)
        sun_rays.set_z_index(1.5)

        self.play(FadeIn(glow_circle, scale=2), *[FadeIn(ray) for ray in sun_rays], run_time=2)

        # Teksti brenda diellit, në dy rreshta
        welcome_line1 = Text(
            "Mirë se erdhët",
            font_size=48,
            weight=BOLD,
            color=WHITE,
            stroke_color=YELLOW,
            stroke_width=2
        ).move_to(UP * 0.3).set_z_index(3)

        welcome_line2 = Text(
            "yje!",
            font_size=48,
            weight=BOLD,
            color=WHITE,
            stroke_color=YELLOW,
            stroke_width=2
        ).next_to(welcome_line1, DOWN, buff=0.05).set_z_index(3)

        self.play(Write(welcome_line1), run_time=1.5)
        self.play(Write(welcome_line2), run_time=1.5)
        self.wait(1)

        # Lëvizje e lehtë për yjet
        self.play(
            stars.animate.shift(DOWN * 0.3 + RIGHT * 0.1),
            run_time=2,
            rate_func=there_and_back
        )

        # Shkëlqim për disa yje
        flashing = AnimationGroup(
            *[
                star.animate.set_opacity(0.2).set_opacity(1).scale(1.1).scale(1/1.1).rotate(PI/20)
                for star in stars[::10]
            ],
            lag_ratio=0.1
        )
        self.play(flashing, run_time=3)

        self.wait(2)
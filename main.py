from manim import *
import numpy as np


class SquarePro(Scene):
    def construct(self):
        # ----------------- SVG INTRO -----------------
        img = SVGMobject("images.svg")
        self.play(Create(img), run_time=3)
        self.wait(1)
        self.play(FadeOut(img), run_time=3)
        self.wait(1)

        # ----------------- AXES -----------------
        axes = Axes(
            x_range=[-50, 60, 10],
            y_range=[-2.5, 2.5, 1],
            x_length=10,
            y_length=6,
            tips=True,
        ).add_coordinates()
        axes.to_edge(LEFT, buff=0)
        self.play(Create(axes))

        # ----------------- SINE WAVE -----------------
        graph = axes.plot(
            lambda x: np.sin(x / 10),
            x_range=[-50, 60],
            color=BLUE,
        )
        self.play(Create(graph), run_time=3)

        # ----------------- SAMPLE VALUES -----------------
        x_vals = [-50, -30, -10, 10, 30, 50]
        y_vals = [np.sin(x / 10) for x in x_vals]

        # ----------------- FULL TABLE -----------------
        table_data = [["x", "sin(x/10)"]] + [
            [
                str(x),
                f"{y:.2f}"
            ]
            for x, y in zip(x_vals, y_vals)
        ]

        table = Table(table_data, include_outer_lines=True).scale(0.5)
        table.to_edge(RIGHT, buff=0)

        # Hide all rows except the header initially
        for row in range(1, len(table_data)):
            for col in range(1, 3):
                table.get_entries((row + 1, col)).set_opacity(0)

        self.add(table)

        # ----------------- ANIMATE ROWS + DOTS -----------------
        for i, (x, y) in enumerate(zip(x_vals, y_vals), start=1):
            # Dot on sine wave
            dot = Dot(axes.c2p(x, y), color=YELLOW)
            self.add(dot)  # keep dot above table

            # Fade in the corresponding table row cells linearly
            self.play(
                *[
                    table.get_entries((i + 1, col)).animate.set_opacity(1)
                    for col in range(1, 3)
                ],
                rate_func=linear,
                run_time=0.5,
            )
            self.wait(0.2)
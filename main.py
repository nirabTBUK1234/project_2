



from manim import *
import numpy as np



class SquarePro(Scene):
    def construct(self):

        # Counstruct SVG(Manim pic)
        img = SVGMobject("images.svg")
        Square1 = Square()
        self.play(Create(img),run_time=3)
        self.wait(1)

        # Fade out Manim SVG
        self.play(FadeOut(img), run_time=3)
        self.wait(1)

        # Create Axes
        axes = Axes(
            x_range=[-50, 60, 10],
            y_range=[-2.5, 2.5, 1],
            x_length=10,
            y_length=7,
            tips=True
        ).add_coordinates()
        
        # Add Axes to the Scene(not animation)
        self.add(axes)

        # Create a sine wave 
        graph = axes.plot(
            lambda x: np.sin(x / 10),
            x_range=[-50,60]
        )

        # Create the animation of sine wave graph and the Axes(actual animation)
        self.play(Create(axes))
        self.wait(1)
        self.play(Create(graph))



        
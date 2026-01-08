



from manim import *
import numpy as np



class SquarePro(Scene):
    def construct(self):
        img = SVGMobject("images.svg")
        Square1 = Square()
        self.play(Create(img),run_time=3)
        self.wait(1)
        self.play(FadeOut(img), run_time=3)
        self.wait(1)
        axis = Axes(x_range=[-50, 60, 10],y_range=[-2.5, 2.5, 1],x_length=10,y_length=7,tips=True)
        axis.add_coordinates()
        self.add(axis)
        graph = axis.plot(lambda x: np.sin(x / 10) ,x_range=[-50,60])

        self.play(Create(axis))
        self.wait(1)

        self.play(Create(graph))



        




from manim import *
import numpy as np



class SquarePro(Scene):
    def construct(self):
        img = SVGMobject("images.svg")
        Square1 = Square()
        self.play(Create(img),run_time=3)
        self.wait(1)
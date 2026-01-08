



from manim import *
import numpy as np



class SquarePro(Scene):
    def construct(self):
        Square1 = Square()
        self.play(Create(Square1))
        self.wait(1)
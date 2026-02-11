from manim import *

class nvim(Scene):
    def construct(self) -> None:
        nvim = SVGMobject('/home/imchethanjs/Pictures/neovim.svg', fill_opacity=0.8, color=GREEN)
        t = Text("Neovim", font='Sentient', weight=NORMAL).next_to(nvim, DOWN)
        self.play(Write(nvim), Write(t))
        self.wait(2)

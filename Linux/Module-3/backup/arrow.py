from manim import *


class Errors(Scene):
    def construct(self) -> None:

        c = Circle().to_edge(DOWN)
        rec = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
        arrow = always_redraw(
            lambda: Line(start=rec.get_bottom(), end=c.get_top(), buff=0.2).add_tip()
        )

        self.add(arrow)
        self.play(Create(VGroup(rec, c)))
        self.wait()
        self.play(rec.animate.to_edge(UR))

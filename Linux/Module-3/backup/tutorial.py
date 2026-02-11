from manim import *
from manim.utils.unit import Percent, Pixels


class FirstExample(Scene):
    def construct(self) -> None:
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        green_square = Square(color=GREEN, fill_opacity=0.8)
        green_square.next_to(blue_circle, RIGHT)
        self.add(blue_circle, green_square)


class SecondExample(Scene):
    def construct(self) -> None:
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: (x + 2) * x * (x - 2) / 2, color=RED)
        area = ax.get_area(curve, x_range=(-2, 0))
        self.play(Create(ax, run_time=2), Create(curve, run_time=5))
        self.play(FadeIn(area))
        self.wait(2)


class SquareToCircle(Scene):
    def construct(self) -> None:
        green_square = Square(color=GREEN, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(ReplacementTransform(green_square, blue_circle), run_time=4)
        # diff btwn Transform and ReplacementTransform is that Transform will make the green_square to blue_circle, so after Transformation, the variable green_square references the blue_circle
        self.play(Indicate(blue_circle))
        self.play(FadeOut(blue_circle))
        self.wait(2)


class Positioning(Scene):
    def construct(self) -> None:
        plane = NumberPlane()
        self.add(plane)

        # next_to
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)

        self.add(red_dot, green_dot)

        # shift
        s = Square(color=ORANGE)
        s.shift(2 * UP + 4 * RIGHT)
        self.add(s)

        # move_to
        c = Circle(color=PURPLE)
        c.move_to((-3, -2, 0))
        self.add(c)

        # align_to
        c2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        c2.align_to(s, LEFT)
        c3.align_to(s, RIGHT)
        c4.align_to(s, UP + RIGHT)
        self.add(c2, c3, c4)


class CriticalPoints(Scene):
    def construct(self) -> None:
        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in [(0, 0, 0), UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s = Square(color=RED, fill_opacity=0.5)
        s.move_to((1, 0, 0), aligned_edge=LEFT)
        self.add(s)


class UsefulUnits(Scene):
    def construct(self) -> None:
        for perc in range(5, 50, 5):
            self.add(Circle(radius=perc * Percent(X_AXIS)))
            self.add(Square(side_length=2 * perc * Percent(Y_AXIS), color=YELLOW))

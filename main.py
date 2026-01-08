


def main():
    
    from manim import *
    import numpy as np

    class DoublePendulum(Scene):
        def construct(self):
            # starting angles
            θ1, θ2 = 2.0, 1.0
            L1, L2 = 2.0, 1.5
            origin = np.array([0,0,0])

            def pendulum_points(theta1, theta2):
                x1 = L1 * np.sin(theta1)
                y1 = -L1 * np.cos(theta1)
                x2 = x1 + L2 * np.sin(theta2)
                y2 = y1 - L2 * np.cos(theta2)
                return np.array([x1, y1, 0]), np.array([x2, y2, 0])

            p1, p2 = pendulum_points(θ1, θ2)

            bob1 = Dot(p1, color=BLUE)
            bob2 = Dot(p2, color=GREEN)

            rod1 = Line(origin, p1)
            rod2 = Line(p1, p2)

            self.add(rod1, rod2, bob1, bob2)

            # animate a simple update loop
            for i in range(60):
                θ1 += 0.05
                θ2 += 0.08
                new_p1, new_p2 = pendulum_points(θ1, θ2)
                self.play(
                    bob1.animate.move_to(new_p1),
                    bob2.animate.move_to(new_p2),
                    rod1.animate.put_start_and_end_on(origin, new_p1),
                    rod2.animate.put_start_and_end_on(new_p1, new_p2),
                    run_time=0.1,
                    rate_func=linear
                )

            self.wait(1)

if __name__ == "__main__":
    main()

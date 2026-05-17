from manim import *
import numpy as np

class MagneticFieldSimulation(Scene):
    def construct(self):
        # 1. Elegant Title
        title = Text("Electromagnetic Vector Field", font="Consolas", color=BLUE_A).scale(0.6)
        title.to_edge(UP)

        # 2. FIXED MATH: Correctly pull individual index coordinates out of the 3D point array
        def vortex_math(point):
            x = point[0]  # First element (X coordinate)
            y = point[1]  # Second element (Y coordinate)
            denominator = (x**2 + y**2 + 0.1)**0.5
            return np.array([-y / denominator, x / denominator, 0])

        # 3. Create the Visual 
        field = ArrowVectorField(
            vortex_math,
            x_range=[-4, 4, 0.5],
            y_range=[-3, 3, 0.5],
            colors=[BLUE_E, WHITE, RED_E]
        )

        
        magnetic_core = Dot(color=YELLOW).scale(2)

    
        self.play(Write(title), FadeIn(magnetic_core))
        self.wait(0.5)

        
        self.play(Create(field), run_time=3)
        self.wait(2)



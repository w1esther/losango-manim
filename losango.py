import numpy as np
from manim import *

class AreaLosango(MovingCameraScene):
        
    def construct(self):

        topo_losango = np.array([0, 2, 0])
        direita_losango = np.array([3, 0, 0])
        baixo_losango = np.array([0, -2, 0])
        esquerda_losango = np.array([-3, 0, 0])
        origem = np.array([0, 0, 0])

        label_losango = MathTex(r'Losango')
        label_losango.shift(2.5*UP)

        label_diagonal_maior = MathTex(r'D', color=YELLOW)
        label_diagonal_maior.shift(1.2*RIGHT + 0.4*UP)

        labe_diagonal_menor = MathTex(r'd', color=RED)
        labe_diagonal_menor.shift(0.8*DOWN + 0.4*LEFT)

        losango = Polygon(topo_losango, direita_losango, baixo_losango, esquerda_losango, color=PURPLE_A)

        self.wait()

        losango.set_fill(BLUE, opacity=0.2)

        self.play(Write(losango), FadeIn(label_losango))

        self.wait(2)

        diagonal_maior = Line(esquerda_losango, direita_losango, color=YELLOW)

        diagonal_menor = Line(topo_losango, baixo_losango, color=RED)

        self.play(Create(diagonal_maior), Create(diagonal_menor), FadeIn(labe_diagonal_menor), FadeIn(label_diagonal_maior))

        self.wait(2)

        grupo_tri1 = VGroup()

        # triângulo 1

        tri_1 = Polygon(origem, topo_losango, esquerda_losango, color=PURPLE_A)

        tri_1.set_fill(BLUE, opacity=0.2)

        destaque1 = Line(topo_losango, origem, color=RED)

        destaque2 = Line(origem, esquerda_losango, color=YELLOW)

        grupo_tri1.add(tri_1, destaque1, destaque2)

        # triângulo 2

        grupo_tri2 = VGroup()

        tri_2 = Polygon(origem, topo_losango, direita_losango, color=PURPLE_A)

        tri_2.set_fill(BLUE, opacity=0.2)

        destaque3 = Line(topo_losango, origem, color=RED)

        destaque4 = Line(origem, direita_losango, color=YELLOW)

        grupo_tri2.add(tri_2, destaque3, destaque4)

        # triângulo 3

        grupo_tri3 = VGroup()

        tri_3 = Polygon(origem, baixo_losango, esquerda_losango, color=PURPLE_A)

        tri_3.set_fill(BLUE, opacity=0.2)

        destaque5 = Line(origem, esquerda_losango, color=YELLOW)

        destaque6 = Line(origem, baixo_losango, color=RED)

        grupo_tri3.add(tri_3, destaque5, destaque6)

        # triângulo 4

        grupo_tri4 = VGroup()

        tri_4 = Polygon(origem, direita_losango, baixo_losango, color=PURPLE_A)

        tri_4.set_fill(BLUE, opacity=0.2)

        destaque7 = Line(origem, direita_losango, color=YELLOW)

        destaque8 = Line(origem, baixo_losango, color=RED)

        grupo_tri4.add(tri_4, destaque7, destaque8)

        self.play(FadeIn(grupo_tri1), FadeIn(grupo_tri2), FadeIn(grupo_tri3), FadeIn(grupo_tri4))

        self.play(FadeOut(losango), FadeOut(label_diagonal_maior), FadeOut(labe_diagonal_menor), FadeOut(label_losango), FadeOut(diagonal_maior), FadeOut(diagonal_menor))

        self.wait(2)

        self.play(grupo_tri3.animate.shift(2*UP + 3*RIGHT))

        self.wait(2)

        self.play(grupo_tri4.animate.shift(2*UP + 3*LEFT))

        self.wait(2)

        label_retangulo = MathTex(r'Retangulo')

        label_retangulo.shift(2.5*UP)

        self.play(FadeIn(label_retangulo))

        self.wait(2)

        label_d2 = MathTex(r'\frac{d}{2}', color=RED)

        label_d2.shift(3.4*RIGHT + 1*UP)

        label_D2 = MathTex(r'D', color=YELLOW)

        label_D2.shift(0.4*DOWN)

        self.play(FadeIn(label_d2), FadeIn(label_D2))

        self.wait(2)

        self.play(self.camera.frame.animate.shift(0.8*DOWN))

        self.wait(2)

        label_area_retangulo = MathTex(r'Area Retangulo:')

        label_area_retangulo.shift(1.4*DOWN)

        area_retangulo = MathTex('b_{base} \cdot h_{altura}')

        area_retangulo.shift(2.2*DOWN)

        self.play(FadeIn(label_area_retangulo),  Write(area_retangulo))

        self.wait(2)

        area_retangulo2 = MathTex(r'\frac {D \cdot d}{2}')

        area_retangulo2.shift(2.5*DOWN)

        self.play(Transform(area_retangulo, area_retangulo2), FadeOut(label_retangulo))

        self.wait(2)

        label_area_losango = MathTex(r'AreaLosango:')

        label_area_losango.shift(1.4*DOWN)

        self.play(Transform(label_area_retangulo, label_area_losango))

        self.wait(2)
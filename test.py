import pyxel

CIMA = 0
BAIXO = 1
DIREITA = 2

class Vetor:
    def __init__(self, mouse_x, mouse_y):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

class Bird:
    def __init__(self):
        pyxel.init(200, 200)

        self.bird = [(50, 100)]
        self.direcao = BAIXO
        self.movimento = DIREITA
        pyxel.run(self.update, self.draw)
        pyxel.load('BIRD.pyxel')

    def update(self):
        if pyxel.frame_count % 5 == 0:
            # movimenta de acordo com entrada do usuario
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                self.direcao = CIMA
            else:
                self.direcao = BAIXO


        cabeca= self.bird[0]

        if self.movimento == DIREITA:
            cabeca = (cabeca[0] + 1, cabeca[1])

        if self.direcao == CIMA:
            cabeca = (cabeca[0], cabeca[1] - 2)
        elif self.direcao == BAIXO:
            cabeca = (cabeca[0], cabeca[1] + 2)

        self.bird.insert(0, cabeca)
        self.bird.pop(-1)

    def draw(self):
        pyxel.cls(0)
        for segmento in self.bird:
            pyxel.rect(segmento[0], segmento[1], segmento[0] + 10, segmento[1] + 10, 3)
        #desenha mouse
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 16, 16, 16, 2)

Bird()
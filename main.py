#importo as bibliotecas necessárias
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

class PongPaddle(Widget):
    #guarda a pontuação
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            #aumenta a velocidade da bolinha
            vel = bounced * 1.5
            ball.velocity = vel.x, vel.y + offset

#crio a classe para o widget da bolinha
class PongBall(Widget):
    title = "Pong Game"

    # velocidade da bolinha nos eixos x e y
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # propriedade referencial para que possamos usar a velocidade da bola como
    # uma abreviação, assim como, por exemplo. velocity para velocity_x e velocity_y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # A função ``move`` moverá a bola um passo. Esse
    # será chamado em intervalos iguais para animar a bola
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

#crio a classe para o widget principal (tela)
class PongGame(Widget):
    #conecta o pongapp ao widget criado na regra kv
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    
    #define uma velocidade aleatória x e y para a bola e também redefine a posição
    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        #chama o movimento da bola e move ela
        self.ball.move()

        #quicaa bolinha nas raquetes
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # quica a bolinha no topo da tela
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # Confere se a bolinha marcou ponto
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))
    
    #controla as raquetes
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

#crio a classe para o app
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        #atualiza a posição da bolinha para que haja a animação
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

#inicia o app
if __name__ == '__main__':
    PongApp().run()
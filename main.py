#importo ad bibliotecas
from kivy.app import App
from kivy.uix.widget import Widget

#crio a classe para o widget principal (tela)
class PongGame(Widget):
    pass

#crio a classe para o app
class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
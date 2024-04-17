from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class TelaPrincipal(GridLayout):
    pass

class Telagarcom(GridLayout):
    pass

class RestauranteApp(App):
    def build(self):
        return TelaPrincipal()
    
if __name__ == "__main__":
    RestauranteApp().run()
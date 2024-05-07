from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#defino as configurações da janela
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'heigth', '640')

class TelaPrincipal(Screen):
    pass

class TelaGarcom(Screen):
    pass

class TelaCozinha(Screen):
    pass

class TelaCaixa(Screen):
    pass

class GerenciadorTelas(ScreenManager):
    pass

kv = Builder.load_file('restaurante.kv')

class RstauranteApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    RstauranteApp().run()
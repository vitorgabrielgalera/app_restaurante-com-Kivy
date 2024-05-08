from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import requests

#defino as configurações da janela
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'heigth', '640')

#popup para quando a senha ou o usuario estiverem errados
class PopupErro(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Erro de autenticação"
        self.size_hint = (0.7, 0.4)
        self.auto_dismiss = False

        self.box = BoxLayout(orientation="vertical")
        self.box.add_widget(
            Label(
                text="Usuário ou senha inválidos!"
            )
        )
        self.box.add_widget(
            Button(
                text= "Fechar",
                on_press= self.dismiss
            )
        )

        self.add_widget(self.box)

class TelaLogin(Screen):
    def autenticar(self):
        usuario = self.ids.txt_usuario.text
        senha = self.ids.txt_senha.text

        #Api que armazena os dados do usuario
        url = "https://ae4c-170-231-200-76.ngrok-free.app/restaurante/autenticar"

        #guarda a senha e o nome em uma unica variável
        dados = {"usuario": usuario, "senha": senha}

        #retorna o status code, utilizando os dados
        resposta = requests.post(url, json=dados)

        #confere se o status code deu certo(200)
        if resposta.status_code == 200:
            self.manager.current = "tela_principal"
        
        #abrir o popup caso algo esteja incorreto
        else:
            popup_erro = PopupErro()
            popup_erro.open()
            #PopupErro.open()

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
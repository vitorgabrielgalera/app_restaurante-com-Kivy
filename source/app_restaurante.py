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

#popup para quando a senha ou o usuario estiverem errados utilizando python
#class PopupErro(Popup):
#    def __init__(self, **kwargs):
#        super().__init__(**kwargs)
#        self.title = "Erro de autenticação"
#        self.size_hint = (0.7, 0.4)
#        self.auto_dismiss = False
#
#        self.box = BoxLayout(orientation="vertical")
#        self.box.add_widget(
#            Label(
#                text="Usuário ou senha inválidos!"
#            )
#        )
#        self.box.add_widget(
#            Button(
#                text= "Fechar",
#                on_press= self.dismiss
#            )
#        )
#
#        self.add_widget(self.box)

#popup para quando a senha ou o usuario estiverem errados utilizando kv
class PopupErro(Popup):
    pass

class TelaLogin(Screen):
    def autenticar(self):
        usuario = self.ids.txt_usuario.text
        senha = self.ids.txt_senha.text

        #Api que armazena os dados do usuario
        url = "https://9717-168-232-136-83.ngrok-free.app/restaurante/autenticar"

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        import sqlite3
        
        # Obtem o cardapio a partir do banco de dados
        conn = sqlite3.connect('cardapio.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cardapio')
        self.cardapio = cursor.fetchall()
        conn.close()

        self.cardapio_itens = [item[1] for item in self.cardapio if item[4] == 'Bar']
        #######
        self.pedido_mesa = {
            "mesa": "",
            "cozinha": [],
            "bar": [],
            "status": "pendente"

        }
    
    def atualiza_lista_cardapio(self):

        if self.ids.radio_bar.active:
            self.ids.itens_cardapio.values = [item[1] for item in self.cardapio if item[4] == 'Bar']
        elif self.ids.radio_cozinha.active:
            self.ids.itens_cardapio.values = [item[1] for item in self.cardapio if item[4] == 'Cozinha']

        self.ids.itens_cardapio.text = "Selecione"

    def decrementa_qtd_item(self):
        if int(self.ids.qtd_item.text) > 0:
            self.ids.qtd_item.text = str(int(self.ids.qtd_item.text) - 1)

    def incrementa_qtd_item(self):
        self.ids.qtd_item.text = str(int(self.ids.qtd_item.text) + 1)

    def inclui_pedido_na_lista(self):
        qtd = self.ids.qtd_item.text
        pedido = self.ids.itens_cardapio.text

        if qtd == "0" or pedido == "Selecione":
            return
        
        if self.ids.mesa.text == "Mesa":
            return
        
        self.ids.itens_cardapio.text = "Selecione"
        self.ids.qtd_item.text = "0"

        self.ids.itens_pedido.text += f"\n{qtd} - {pedido}"
        self.pedido_mesa["mesa"] = self.ids.mesa.text

        if self.ids.radio_bar.active:
            self.pedido_mesa["bar"].append(f"{qtd} - {pedido}")
        elif self.ids.radio_cozinha.active:
            self.pedido_mesa["cozinha"].append(f"{qtd} - {pedido}")

    def enviar_pedido(self):
        url = "https://cf9d-168-232-136-83.ngrok-free.app/restaurante/criar_pedido"
        resposta = requests.post(url, json=self.pedido_mesa)

class TelaCozinha(Screen):
    pass

class TelaCaixa(Screen):
    pass

class TelaBar(Screen):
    pass

class GerenciadorTelas(ScreenManager):
    pass

kv = Builder.load_file('restaurante.kv')

class RstauranteApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    RstauranteApp().run()
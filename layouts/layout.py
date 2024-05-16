from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#muda a cor da janela
from kivy.core.window import Window

Window.clearcolor = (120/255.0, 80/255.0, 20/255.0, 1)

class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        #definindo a quantidade de colunas(2)
        self.cols = 1

        self.sub_layout = GridLayout()
        self.sub_layout.cols = 2

        #criando o label nome
        self.nome_label = Label(text='Nome:')
        #adicionando o label ao layout
        self.sub_layout.add_widget(self.nome_label)

        #criando o TextINput do nome
        self.nome_cliente = TextInput(multiline=False)
        #adicionando o TextInput ao layout
        self.sub_layout.add_widget(self.nome_cliente)

#########################################################
        
        #criando o label mesa
        self.mesa_label = Label(text='Mesa:')
        #adicionando o label ao layout
        self.sub_layout.add_widget(self.mesa_label)

        #criando o TextINput da mesa
        self.mesa_label = TextInput(multiline=False)
        #adicionando o TextInput ao layout
        self.sub_layout.add_widget(self.mesa_label)

#########################################################
        
        #criando o label pedido
        self.pedido_label = Label(text='Pedido:')
        #adicionando o label ao layout
        self.sub_layout.add_widget(self.pedido_label)

        #criando o TextINput do pedido
        self.pedido_label = TextInput(multiline=True)
        #adicionando o TextInput ao layout
        self.sub_layout.add_widget(self.pedido_label)

#########################################################
        
        #posiciono o sub layout
        self.add_widget(self.sub_layout)

        #criando o botão enviar
        self.enviar = Button(text = "Enviar Pedido:")
        #adicionando a função callback
        self.enviar.bind(on_press=self.enviar_pedido)
        #adicionando o botão
        self.add_widget(self.enviar)

    def enviar_pedido(self, instance):
        #criando o label de confirmação
        self.confirmacao = Label(text=f"Cliente : {self.nome_cliente.text}\nMesa: {self.mesa_label.text}\nPedido: {self.pedido_label.text}")
        #posicionando a confirmação
        self.add_widget(self.confirmacao)
        #limpando o campo de texto
        self.nome_cliente.text = ' '
        self.mesa_label.text = ' '
        self.pedido_label.text = ' '

#Cria o objeto do app
class LanchoneteApp(App):
    def build(self):
        return MainLayout()
    
# Inicia o aplicativo
if __name__ == '__main__':
    LanchoneteApp().run()
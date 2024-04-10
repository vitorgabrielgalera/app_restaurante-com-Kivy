#importo as bibliotecas
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

#crio minha classe do layout
class MainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainGridLayout, self).__init__(**kwargs)
        
        #defino a quantidade de colunas, de espaçamento entre os botões e o tamnho da borda
        self.cols = 2
        self.spacing = 2
        self.padding = 6

        #adiciono o primeito botão
        self.add_widget(Button(text="Main GridLayout 1"))

        #crio um layout secundário para outros botões
        self.segundo_layout = GridLayout(cols=1, spacing = 2)
        #coloco três botões no layout secundário
        self.segundo_layout.add_widget(Button(text="Second GridLayout 1"))
        self.segundo_layout.add_widget(Button(text="Second GridLayout 2"))
        self.segundo_layout.add_widget(Button(text="Second GridLayout 3"))

        #coloco o layout secundário no layout principal
        self.add_widget(self.segundo_layout)

        #crio o restante dos botões
        self.add_widget(Button(text="Main GridLayout 2"))
        self.add_widget(Button(text="Main GridLayout 3"))
        self.add_widget(Button(text="Main GridLayout 4"))
        self.add_widget(Button(text="Main GridLayout 5"))
        self.add_widget(Button(text="Main GridLayout 6"))
        self.add_widget(Button(text="Main GridLayout 7"))

#inicio meu layout
class GridlayoutApp(App):
    def build(self):
        return MainGridLayout()
    
#inicio o programa
if __name__ == "__main__":
    GridlayoutApp().run()
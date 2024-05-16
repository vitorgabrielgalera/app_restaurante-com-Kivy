#importo as bibliotecas
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

#crio minha classe do layout
class MainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainGridLayout, self).__init__(**kwargs)

        self.cols = 2
        self.rows = 2
        self.spacing = 2
        self.padding = 6

        #crio o botão maior
        self.add_widget(Button(text="Button 1"))

        #crio o segundo layout e posiciono os botões dentro dele
        self.segundo_layout = GridLayout(cols=1, spacing = 2)
        self.segundo_layout.add_widget(Button(text="Button 2"))
        self.segundo_layout.add_widget(Button(text="Button 3"))
        self.segundo_layout.add_widget(Button(text="Button 4"))

        self.add_widget(self.segundo_layout)

        #crio o terceiro layout e posiciono os botões dentro dele
        self.terceiro_layout = GridLayout(cols=2, spacing = 2)
        self.terceiro_layout.add_widget(Button(text="Button 5"))
        self.terceiro_layout.add_widget(Button(text="Button 6"))
        self.terceiro_layout.add_widget(Button(text="Button 7"))
        self.terceiro_layout.add_widget(Button(text="Button 8"))

        self.add_widget(self.terceiro_layout)

        #crio o quarto layout e posiciono os botões dentro dele
        self.quarto_layout = GridLayout(cols=3, spacing = 2)
        self.quarto_layout.add_widget(Button(text="Button 6"))
        self.quarto_layout.add_widget(Button(text="Button 7"))
        self.quarto_layout.add_widget(Button(text="Button 8"))

        self.add_widget(self.quarto_layout)

#inicio meu layout
class GridlayoutApp(App):
    def build(self):
        return MainGridLayout()

#inicio o programa    
if __name__ == "__main__":
    GridlayoutApp().run()
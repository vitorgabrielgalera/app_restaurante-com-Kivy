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

        self.add_widget(Button(text="Button 1"))

        self.segundo_layout = GridLayout(cols=1, spacing = 2)
        self.segundo_layout.add_widget(Button(text="Button 2"))
        self.segundo_layout.add_widget(Button(text="Button 3"))
        self.segundo_layout.add_widget(Button(text="Button 4"))

        self.add_widget(self.segundo_layout)

#inicio meu layout
class GridlayoutApp(App):
    def build(self):
        return MainGridLayout()

#inicio o programa    
if __name__ == "__main__":
    GridlayoutApp().run()
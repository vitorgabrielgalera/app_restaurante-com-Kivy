from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainGridLayout, self).__init__(**kwargs)

        self.cols = 2
        self.rows = 2
        self.spacing = 2
        self.padding = 6

        self.add_widget(Button(text="Button 1"))

        self.segundo_layout = GridLayout(cols=1, spacing = 2)
        self.segundo_layout.add_widget(Button(text="Button 2"))
        self.segundo_layout.add_widget(Button(text="Button 3"))
        self.segundo_layout.add_widget(Button(text="Button 4"))

        self.add_widget(self.segundo_layout)

        self.terceiro_layout = GridLayout(cols=2, spacing = 2)
        self.terceiro_layout.add_widget(Button(text="Button 5"))
        self.terceiro_layout.add_widget(Button(text="Button 6"))
        self.terceiro_layout.add_widget(Button(text="Button 7"))
        self.terceiro_layout.add_widget(Button(text="Button 8"))

        self.add_widget(self.terceiro_layout)

        self.quarto_layout = GridLayout(cols=3, spacing = 2)
        self.quarto_layout.add_widget(Button(text="Button 6"))
        self.quarto_layout.add_widget(Button(text="Button 7"))
        self.quarto_layout.add_widget(Button(text="Button 8"))

        self.add_widget(self.quarto_layout)



class GridlayoutApp(App):
    def build(self):
        return MainGridLayout()
    
if __name__ == "__main__":
    GridlayoutApp().run()
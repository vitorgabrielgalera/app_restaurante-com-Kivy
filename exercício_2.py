from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainGridLayout, self).__init__(**kwargs)

        self.cols = 2
        self.spacing = 2
        self.padding = 6

        self.add_widget(Button(text="Button 1"))

        self.segundo_layout = GridLayout(cols=1, spacing = 2)
        self.segundo_layout.add_widget(Button(text="Button 2"))
        self.segundo_layout.add_widget(Button(text="Button 3"))
        self.segundo_layout.add_widget(Button(text="Button 4"))

        self.add_widget(self.segundo_layout)



class GridlayoutApp(App):
    def build(self):
        return MainGridLayout()
    
if __name__ == "__main__":
    GridlayoutApp().run()
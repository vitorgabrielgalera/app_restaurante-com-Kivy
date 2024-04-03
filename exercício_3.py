from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainGridLayout, self).__init__(**kwargs)

        self.cols = 3
        self.rows = 3
        self.spacing = 2
        self.padding = 6
        
        self.add_widget(Button(text="Button 1"))
        self.add_widget(Label(text=""))
        self.add_widget(Button(text="Button 2"))
        self.add_widget(Label(text=""))
        self.add_widget(Button(text="Button 3"))
        self.add_widget(Label(text=""))
        self.add_widget(Button(text="Button 4"))
        self.add_widget(Label(text=""))
        self.add_widget(Button(text="Button 5"))


class GridlayoutApp(App):
    def build(self):
        return MainGridLayout()
    
if __name__ == "__main__":
    GridlayoutApp().run()
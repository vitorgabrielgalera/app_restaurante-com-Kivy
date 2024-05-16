from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MainGridLayout(GridLayout):
    pass

class MyGridLayoutApp(App):
    def build(self):
        return MainGridLayout()
    
#class SecondGridLayout(GridLayout):
#    pass
    
if __name__ == "__main__":
    MyGridLayoutApp().run()
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MainGridLayout(GridLayout):
    pass

class Exer2App(App):
    def build(self):
        return MainGridLayout()
    
#class SecondGridLayout(GridLayout):
#    pass
    
if __name__ == "__main__":
    Exer2App().run()
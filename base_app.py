from kivy.app import App
from kivy.uix.widget import Widget

class BaseApp(App):
    def build(self):
        return Widget()
    
if __name__ == "__main__":
    BaseApp().run()
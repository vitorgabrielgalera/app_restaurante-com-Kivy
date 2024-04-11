from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainBoxLayout, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.add_text = Button(text="add text label")
        self.add_widget(self.add_text)
        self.add_text.bind(on_press=self.add_text_label)

        self.remove_text = Button(text="remove text label")
        self.add_widget(self.remove_text)
        self.remove_text.bind(on_press=self.remove_text_label)

    def add_text_label(self, instance):
        self.add_widget(Label(text="Texto 1"))

    def remove_text_label(self, instance):
        if self.children:
            self.remove_widget(self.children[0])

class BoxLayoutApp(App):
    def build(self):
        return MainBoxLayout()
    
if __name__ == "__main__":
    BoxLayoutApp().run()
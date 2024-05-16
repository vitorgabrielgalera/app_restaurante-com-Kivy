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
        
        self.label_list = []

    def add_text_label(self, instance):
        tamanho = len(self.children)
        label = Label(text=f"{tamanho}")
        self.add_widget(label, index=tamanho)
        self.label_list.append(label)

    def remove_text_label(self, instance):
        if len(self.children) > 2:
            #self.remove_widget(self.children[len(self.children)-1])
            self.remove_widget(self.label_list.pop())

class BoxLayoutApp(App):
    def build(self):
        return MainBoxLayout()
    
if __name__ == "__main__":
    BoxLayoutApp().run()
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class MainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(MainWindow ,self).__init__(**kwargs)

        self.btn1 = Button(text="Button 1",
            size_hint=(0.2,0.2),
            pos_hint={'left':1, 'top':1}
            )
        self.add_widget(self.btn1)

        self.btn2 = Button(text="Button 2",
            size_hint=(0.2,0.2),
            pos_hint={'right':1, 'top':1}
            )
        self.add_widget(self.btn2)

        self.btn3 = Button(text="Button 3",
            #size_hint=(0.2,0.2),
            size_hint = (None, None),
            size=(150,50) ,
            pos_hint={'x':0.4,'y':0.4}
            #pos=(300,450)
            )
        self.add_widget(self.btn3)

        self.btn4 = Button(text="Button 4",
            size_hint=(0.2,0.2),
            pos_hint={'x':0, 'y':0}
            )
        self.add_widget(self.btn4)

        self.btn5 = Button(text="Button 5",
            size_hint=(0.2,0.2),
            pos_hint={'right':1, 'y':0}
            )
        self.add_widget(self.btn5)


class FloatApp(App):
    def build(self):
        return MainWindow()
    
if __name__ == "__main__":
    FloatApp().run()
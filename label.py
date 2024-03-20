from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MyWidget(Widget):
    pass

#Cria o objeto do app
class LabelApp(App):
    #Este método é chamado quando aplicativo é iniciado
    #Deve sempre se chamar build
    def build(self):

        #Mérodos para criar e manipular um label

        #label = Label(
        #    text = "Hello World!",
        #    font_size = "50sp",
        #    bold = True,
        #    italic = True,
        #    color = (166/255.0, 213/255.0, 255/255.0, 1),
        #    #posiciona o texto
        #    halign = "left",
        #    valign = "middle",
        #    text_size =(400, 400)
        #)

        return MyWidget()
    
# Inicia o aplicativo
if __name__ == '__main__':
    LabelApp().run()
from kivy.app import App
#from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):
    pass

class MyApp(App):
    def build(self):

        return Container()

MyApp().run()

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Container(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = 0

    def display_name(self, name):
        self.score += 1
        print('dn:', name, self.score)
        self.ids.display_label.text = f'Hello {name} -> {self.score}'

class Denseeksnake(App):
    def build(self):
        return Container()
    
if __name__ == "__main__":
    Denseeksnake().run()


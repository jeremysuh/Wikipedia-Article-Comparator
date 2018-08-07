import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

import wikipedia

class GridLayout2(GridLayout):
    pass

class CustomLayoutApp(App):
    def build(self):
        return GridLayout2()

app = CustomLayoutApp()
app.run()
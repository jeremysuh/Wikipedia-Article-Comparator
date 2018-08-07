import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, AsyncImage

import wikipedia


class GridLayout2(GridLayout):
    pass

class CustomLayoutApp(App):
    def build(self):


        return GridLayout2()



app = CustomLayoutApp()
app.run()
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, AsyncImage
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.loader import Loader

import wikipedia
import matplotlib



class MainLayout(GridLayout):

    label_wid = ObjectProperty()

    def change_text(self):
        pass

class TempLayout(FloatLayout):


    def change_text(self):

        pass

    pass

class WikipediaComparatorApp(App):
    def build(self):

        Loader.loading_image = 'tenory.gif'
        Loader.error_image = 'cat.png'
        Config.set('graphics', 'width', '1024')
        Config.set('graphics', 'height', '640')
        Config.set('graphics', 'resizable', '0')
        return TempLayout()



app = WikipediaComparatorApp()
app.run()
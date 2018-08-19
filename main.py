import kivy

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, AsyncImage
from kivy.uix.textinput import TextInput

import wikipedia


class MainLayout(GridLayout):

    label_wid = ObjectProperty()

    def change_text(self, num):
        print "fire"
        if num == 5:
            self.ids.sixbutton.text = 'woter'
            self.ids.firstpic.source = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Wendy_Son_at_Dream_Concert_on_May_12%2C_2018.jpg/800px-Wendy_Son_at_Dream_Concert_on_May_12%2C_2018.jpg"
        else:
            self.ids.sixbutton.text = 'fore'


    pass

class WikipediaComparatorApp(App):
    def build(self):

        return MainLayout()



app = WikipediaComparatorApp()
app.run()
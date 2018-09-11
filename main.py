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
from math import sin


import wikipedia

import matplotlib
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg,\
                                                NavigationToolbar2Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import numpy as np


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4

matplotlib.rcParams.update({'font.size': 8})


objects = ('Python', 'C++', 'Java', 'Perl', 'Scala')
y_pos = np.arange(len(objects))
performance = [10, 8, 6, 4, 2]


plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Most frequent words')




class TempLayout(FloatLayout):

    def on_click_check(self):
        self.ids.destination.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.ids.destination2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        pass

    def on_click_random(self):

        pass

    def on_click_compare(self):

        pass

    def analyze_and_compare(self):

        pass


    def change_text(self):

        pass

    pass

class WikipediaComparatorApp(App):
    def build(self):

        Loader.loading_image = 'tenory.gif'
        Loader.error_image = 'cat.png'
        Config.set('graphics', 'width', '1200')
        Config.set('graphics', 'height', '640')
        Config.set('graphics', 'resizable', '0')
        return TempLayout()



app = WikipediaComparatorApp()
app.run()
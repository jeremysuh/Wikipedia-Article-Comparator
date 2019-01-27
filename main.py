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
import numpy as np2


import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size': 8})



class MainLayout(FloatLayout):

    current_page = 2;
    first_input_confirm = False
    second_input_confirm = False
    article_one = ""
    article_two = ""
    article_one_dictionary = []
    article_two_dictionary = []
    article_one_freq_words = []
    article_two_freq_words = []
    article_one_performance = []
    article_two_performance = []

    def hide_show_graphs(self):

        if self.current_page is 1:
            self.current_page = 2
            self.ids.green_bar.pos_hint = {"x":0.075,"y":0.075}
            self.ids.red_bar.pos_hint = {"x":0.075,"y":0.075}
            self.ids.destination.size_hint_y = 0.45
        else:
            self.current_page = 1
            self.ids.green_bar.pos_hint = {"x":0.075,"y":-1}
            self.ids.red_bar.pos_hint = {"x":0.075,"y":-1}
            self.ids.destination.size_hint_y = 0

        pass

    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)

        fig = plt.figure()
        f, ((ax1, ax2)) = plt.subplots(1, 2, sharex=False, sharey=False)

        x = [0, 1, 2, 3, 4]
        ax2.set_xticks(np.arange(min(x), max(x) + 1, 1.0))
        ax1.set_xticks(np.arange(min(x), max(x) + 1, 1.0))

        objects = ('Python', 'C++', 'Java', 'Perl', 'Scala')
        y_pos = np.arange(len(objects))
        performance = [5,5,5,5,5]
        ax1.bar(y_pos, performance, align='center', alpha=0.5)

        ax1.set_xticklabels(('-','-','-','-','-'))
        ax2.set_xticklabels(('-','-','-','-','-'))

        plt.suptitle('Most frequent words')
        y_pos = np.arange(len(objects))
        performance = [5,5,5,5,5]
        ax2.bar(y_pos, performance, align='center', alpha=0.5)


        self.ids.destination.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.hide_show_graphs()


    def on_click_check(self, num):


        if num is 1:
            try:
                wikipedia.search(self.ids.search_one.text)

                article = wikipedia.page(self.ids.search_one.text)
                self.article_one = self.ids.search_one.text
                self.first_input_confirm = True
                if self.first_input_confirm & self.second_input_confirm:
                    self.ids.compare_button.disabled = False

            except wikipedia.WikipediaException:
                self.ids.compare_button.disabled = True
        else:
            try:

                article = wikipedia.page(self.ids.search_two.text)

                self.article_two = self.ids.search_two.text
                self.second_input_confirm = True
                if self.first_input_confirm & self.second_input_confirm:
                    self.ids.compare_button.disabled = False
            except wikipedia.WikipediaException:
                self.ids.compare_button.disabled = True

        pass

    def analyze(self, article, num, title, image, links, section, reference, word_count, unique_words):
        print "analyze"

        wikiarticle = wikipedia.page(article)
        title.text = "Article Title: " + article
        image.text = "Image Count: " + str(self.count_images(wikiarticle, num))
        links.text = "Link Count: " + str(self.count_links(wikiarticle))
        section.text = "Categories Count: " + str(self.count_section(wikiarticle))
        reference.text = "Reference Count: " + str(self.count_reference(wikiarticle))
        word_count.text = "Word Count: " + str(self.count_word(wikiarticle))
        self.analyze_words(wikiarticle, unique_words, num)


    def analyze_words(self, article, unique_words, num):


        dictionary = {}
        text = article.content
        textsplit = text.split()

        for word in textsplit:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

        unique_words.text = "Unique Words: " + str(len(dictionary))

        if num is 1:
            self.article_one_dictionary = dictionary
        else:
            self.article_two_dictionary = dictionary


        pass

    def get_frequent_words(self, dictionary, num):
        print num

        objects = []
        performance = []
        for i in range(0, 5):

            largestCount = 0
            frequentWord = ""

            for key in dictionary:
                if dictionary[key] > largestCount:
                    frequentWord = key
                    largestCount = dictionary[key]

            objects.append(frequentWord)
            performance.append(largestCount)

            del dictionary[frequentWord]


        if num is 1:
            print("FIRST")
            self.article_one_freq_words = objects
            self.article_one_performance = performance
        else:
            print("SECOND")
            self.article_two_freq_words = objects
            self.article_two_performance = performance

        pass

    def update_graphs(self):

        self.ids.destination.clear_widgets()

        fig = plt.figure()
        f, ((ax1, ax2)) = plt.subplots(1, 2, sharex=False, sharey=False)

        x = [0, 1, 2, 3, 4]
        ax2.set_xticks(np.arange(min(x), max(x) + 1, 1.0))
        ax1.set_xticks(np.arange(min(x), max(x) + 1, 1.0))

        objects = ('Python', 'C++', 'Javap', 'Perlp', 'Scala')
        y_pos = np.arange(len(objects))
        performance = self.article_one_performance
        ax1.bar(y_pos, performance, align='center', alpha=0.5)
        ax1.set_xticklabels(self.article_one_freq_words)

        ax2.set_xticklabels(self.article_two_freq_words)
        plt.suptitle('Most frequent words')
        y_pos = np.arange(len(objects))

        performance = self.article_two_performance
        ax2.bar(y_pos, performance, align='center', alpha=0.5)

        self.ids.destination.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        pass

    def count_word(self, wikiarticle):

        text = wikiarticle.content
        return len(map(len, text.split()))


    def count_images(self, wikiarticle, num):

    #    if num is 1:
        #    if len(wikiarticle.images) != 0:
             #   self.ids.wiki_image_one.source = wikiarticle.images[0]

      #  else:
         #   if len(wikiarticle.images) != 0:
              #  self.ids.wiki_image_two.source = wikiarticle.images[0]

        return len(wikiarticle.images)

    def count_links(self, wikiarticle):

        return len(wikiarticle.links)

    def count_section(self, wikiarticle):

        return len(wikiarticle.categories)

    def count_reference(self, wikiarticle):

        return len(wikiarticle.references)


    def on_click_arrow(self):
        self.hide_show_graphs()
        pass


    def on_click_compare(self):
        print "compare"
        print self.article_one
        self.analyze(self.article_one, 1,
                     self.ids.article_title_one,
                     self.ids.image_count_one,
                     self.ids.link_count_one,
                     self.ids.section_count_one,
                     self.ids.reference_count_one,
                     self.ids.word_count_one,
                     self.ids.unique_words_one

                     )
        self.analyze(self.article_two, 2,
                     self.ids.article_title_two,
                     self.ids.image_count_two,
                     self.ids.link_count_two,
                     self.ids.section_count_two,
                     self.ids.reference_count_two,
                     self.ids.word_count_two,
                     self.ids.unique_words_two
        )

        self.ids.green_bar.size_hint_x = self.compare_dictionary(self.article_one_dictionary, self.article_two_dictionary) * 0.85
        self.get_frequent_words(self.article_one_dictionary, 1)
        self.get_frequent_words(self.article_two_dictionary, 2)

        self.update_graphs()

        pass

    def on_click_random(self, num):

        random_text = wikipedia.random()
        while (len(random_text) >= 17):
            random_text = wikipedia.random()

        if num is 1:

            self.ids.search_one.text = random_text
            self.ids.compare_button.disabled = True
        else:
            self.ids.search_two.text = random_text
            self.ids.compare_button.disabled = True

        pass

    def compare_dictionary(self, d1, d2):

        similar_words = 0
        for key in d1:
            if key in d2:
                similar_words+=1

        return float(similar_words)/(similar_words + (len(d1)-similar_words) + (len(d2)-similar_words))


    def change_text(self):


        pass

    pass

class WikipediaComparatorApp(App):
    def build(self):

        Loader.loading_image = 'tenory.gif'
        Loader.error_image = 'wikilogo.png'
        Config.set('graphics', 'width', '1500')
        Config.set('graphics', 'height', '640')
        Config.set('graphics', 'resizable', '0')
        return MainLayout()



app = WikipediaComparatorApp()
app.run()
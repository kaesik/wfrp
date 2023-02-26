import random

from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.gridlayout import GridLayout

from mutations import *

Builder.load_file("losowanie.kv")


class MutationPhysical(GridLayout):
    description = StringProperty("--")
    effect = StringProperty("--")

    def on_button_click_random(self):
        print("Button clicked")
        self.description, self.effect = random.choices([*MutationsPhysical.keys()], MutationsPhysical.values(), k=1)[0]


class MutationMental(GridLayout):
    description = StringProperty("--")
    effect = StringProperty("--")

    def on_button_click_random(self):
        print("Button clicked")
        self.description, self.effect = random.choices([*MutationsMental.keys()], MutationsMental.values(), k=1)[0]

class MutationAdvanced(GridLayout):
    description = StringProperty("--")
    effect = StringProperty("--")

    def on_button_click_random(self):
        print("Button clicked")
        self.description, self.effect = random.choices([*MutationsAdvanced.keys()], MutationsAdvanced.values(), k=1)[0]

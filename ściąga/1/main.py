from kivy.app import App
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior

from http_client import HttpClient
from models import Pizza
from storage_manager import StorageManager


class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()

class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)

    def op_parent(self, widget, parent):
        pizza_dict = StorageManager().load_data("pizzas")
        if pizza_dict:
            self.recycleView.data = pizza_dict

    def on_server_data(self, pizza_dict):
        self.recycleView.data = pizza_dict
        StorageManager().save_data("pizzas", pizza_dict)

    def on_server_error(self, error):
        print("ERROR " + error)
        self.error_str = "ERROR " + error


class PizzaApp(App):
    pass


PizzaApp().run()

from kivy.app import App
from kivy.properties import *
from navigation_screen_manager import NavigationScreenManager


class MyScreenManager(NavigationScreenManager):
    pass


class WarhammerApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager


WarhammerApp().run()

from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_file("widget_examples.kv")

class WidgetExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    text_input_str = StringProperty("text")

#przycisk dodający 1
    def on_button_click_plus(self):
        print("Button clicked")
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

#przycisk odejmujący 1
    def on_button_click_minus(self):
        print("Button clicked")
        if self.count_enabled:
            self.count -= 1
            self.my_text = str(self.count)

#przycisk włączający poprzdnie przyciski, tj +1 i -1
    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "Edytowanie wyłączone"
            self.count_enabled = False
        else:
            widget.text = "Edytowanie włączone"
            self.count_enabled = True

#switch co nic nie robi
    def on_switch_button_active(self, widget):
        print("switch: " + str(widget.active))


    def on_text_validate(self, widget):
        self.text_input_str = widget.text
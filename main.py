from kivy.app import App
# from kivy.uix.button import Button
# from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class WidgetsExample(BoxLayout):
    count = 0
    slider_value = 50
    # count_label_text = StringProperty(str(count))
    # slider_value_text = StringProperty(str(slider_value))
    # toggle_button_state = StringProperty("Off")

    def button_toggle(self, widget):
        if widget.state == "down":
            widget.text = "On"
            self.ids.count_button.disabled = False
        else:
            widget.text = "Off"
            self.ids.count_button.disabled = True

    def button_change_label_text(self):
        self.count += 1
        self.ids.counter_label.text = str(self.count)

    # def on_switch_active(self, widget):
    #     self.ids.slider.disabled = not widget.active
    #     print("Switch " + ("On" if widget.active else "Off"))

    def on_slider_value(self, widget):
        self.slider_value = int(widget.value)
        # self.slider_value_text = str(self.slider_value)
        # self.ids.slider_label.text = str(self.slider_value)
    def on_text_validate(self, widget):
        self.ids.text_input_label.text = widget.text
    # pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()

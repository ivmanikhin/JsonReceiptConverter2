from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    count = 0
    label_text = StringProperty("0")
    toggle_button_state = StringProperty("0")

    def button_toggle(self, widget):
        self.toggle_button_state = str(widget.state)

    def button_change_label_text(self):
        self.count += 1
        self.label_text = str(self.count)

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

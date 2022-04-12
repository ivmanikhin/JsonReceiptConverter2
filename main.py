from kivy.app import App
import json
# from kivy.uix.button import Button
# from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget





class WidgetsExample(BoxLayout):
    # count = 0
    # slider_value = 50
    # # count_label_text = StringProperty(str(count))
    # # slider_value_text = StringProperty(str(slider_value))
    # # toggle_button_state = StringProperty("Off")
    #
    # def button_toggle(self, widget):
    #     if widget.state == "down":
    #         widget.text = "On"
    #         self.ids.count_button.disabled = False
    #     else:
    #         widget.text = "Off"
    #         self.ids.count_button.disabled = True
    #
    # def button_change_label_text(self):
    #     self.count += 1
    #     self.ids.counter_label.text = str(self.count)
    #
    # # def on_switch_active(self, widget):
    # #     self.ids.slider.disabled = not widget.active
    # #     print("Switch " + ("On" if widget.active else "Off"))
    #
    # def on_slider_value(self, widget):
    #     self.slider_value = int(widget.value)
    #     # self.slider_value_text = str(self.slider_value)
    #     # self.ids.slider_label.text = str(self.slider_value)
    # def on_text_validate(self, widget):
    #     self.ids.text_input_label.text = widget.text

    def json_receipt_to_text(self, uri):
        try:
            with open(uri.replace('"', ''), "r", encoding="utf-8") as file:
                json_receipt = json.load(file)
            text_receipt = f"{json_receipt['retailPlace']}\n" \
                           f"{json_receipt['localDateTime'].replace('T', ' ')}:00\n"
            for item in json_receipt["items"]:
                text_receipt += f"{item['name']}  ({item['quantity']}) - {'{:.2f}'.format(item['sum'] * 0.01)}\n"
            text_receipt += f"{'{:.2f}'.format(json_receipt['totalSum'] * 0.01)} р."
            self.ids.text_input.text = text_receipt
        except Exception as e:
            self.ids.text_input.text = str(e)
            pass
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
    # from jnius import autoclass
    #
    # # test for an intent passed to us
    # PythonActivity = autoclass('org.renpy.android.PythonActivity')
    # activity = PythonActivity.mActivity
    # intent = activity.getIntent()
    # intent_data = intent.getData()
    # try:
    #     file_uri = intent_data.toString()
    #     WidgetsExample.json_receipt_to_text(file_uri)
    # except AttributeError:
    #     file_uri = None


TheLabApp().run()





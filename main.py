from functools import partial

from kivy.app import App
import json
from kivy.uix.button import Button
# from kivy.properties import StringProperty

from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
import os


class MainWidget(ScrollView):
    dir_buttons = []

    def json_receipt_to_text(self, uri, btn=None):
        for dir_button in self.dir_buttons:
            self.ids.main_layout.remove_widget(dir_button)
        self.dir_buttons.clear()
        if ".json" in uri:
            print("FOUND JSON")
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
        else:
            try:
                dir_list = os.listdir(uri)
                print(dir_list)
                for _ in range(len(dir_list)):
                    full_path = uri + "\\" + dir_list[_]
                    print(full_path)
                    self.dir_buttons.append(Button(text=dir_list[_], size_hint=(1, None), height="40dp",
                                                   halign='left',
                                                   on_press=partial(self.json_receipt_to_text, full_path)))
                    self.ids.main_layout.add_widget(self.dir_buttons[_])
                # for dir_button in self.dir_buttons:
                #     dir_button.bind(on_press=partial(self.json_receipt_to_text, uri + "\\" + dir_button.text))
                #     self.ids.main_layout.add_widget(dir_button)
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


class JsonReceiptConverterApp(App):
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


JsonReceiptConverterApp().run()





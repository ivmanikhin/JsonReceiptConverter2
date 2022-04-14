from functools import partial

from kivy.app import App
import json

from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.button import Button
# from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
import os
from jnius import autoclass



PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
String = autoclass('java.lang.String')

StrictMode = autoclass('android.os.StrictMode')



class MainWidget(ScrollView):
    dir_buttons = []

    def share(self, message):
        intent = Intent()
        intent.setAction(Intent.ACTION_SEND)
        intent.putExtra(Intent.EXTRA_TEXT, String(message))
        intent.setType('text/plain')
        chooser = Intent.createChooser(intent, String('Share...'))
        PythonActivity.mActivity.startActivity(chooser)

    def convert_json_to_text(self, json_item, extra_zeros=True, btn=None):
        text_receipt = f"**{json_item['retailPlace']}**\n" \
                       f"{json_item['localDateTime'].replace('T', ' ')}:00\n" if extra_zeros else f"**{json_item['retailPlace']}**\n" \
                                                                                                  f"{json_item['localDateTime'].replace('T', ' ')}\n"
        for item in json_item["items"]:
            text_receipt += f"{item['name']}  ({item['quantity']}) - {'{:.2f}'.format(item['sum'] * 0.01)}\n"
        text_receipt += f"**{'{:.2f}'.format(json_item['totalSum'] * 0.01)} р.**"
        self.ids.converted_json.text = text_receipt
        Clipboard.copy(text_receipt)
        if btn != None:
            btn.background_color = "blue"

    def convert_batch_json_to_text(self, raw_json, btn=None):
        for dir_button in self.dir_buttons:
            self.ids.main_layout.remove_widget(dir_button)
        self.dir_buttons.clear()
        try:
            if not "ticket" in raw_json[0].keys():
                for _ in range(len(raw_json)):
                    self.dir_buttons.append(Button(text=raw_json[_]['localDateTime'].replace('T', ' ') + ":00\n" + raw_json[_]['retailPlace'] + "\n" + '{:.2f}'.format(raw_json[_]['totalSum'] * 0.01) + " р.",
                                                   size_hint=(1, None), height="80dp", split_str="True", text_size=(Window.width - dp(20), None),
                                                   on_press=partial(self.convert_json_to_text, raw_json[_], True)))
                    self.ids.main_layout.add_widget(self.dir_buttons[_])
            else:
                # print("Ticket length: " + str(len(raw_json)))
                for _ in range(len(raw_json)):
                    json_item = raw_json[_]["ticket"]["document"]["receipt"]
                    # print(json_item)
                    json_item['localDateTime'] = json_item['dateTime']
                    self.dir_buttons.append(Button(text=json_item['localDateTime'].replace('T', ' ') + "\n" + json_item['retailPlace'] + "\n" + '{:.2f}'.format(json_item['totalSum'] * 0.01) + " р.",
                                                   size_hint=(1, None), height="80dp", split_str="True", text_size=(Window.width - dp(20), None),
                                                   on_press=partial(self.convert_json_to_text, json_item, False)))
                    self.ids.main_layout.add_widget(self.dir_buttons[_])
        except Exception as e:
            self.ids.converted_json.text = str(e)
            pass

    def read_json(self, uri, btn=None):
        try:
            with open(uri.replace('"', ''), "r", encoding="utf-8") as file:
                json_receipt = json.load(file)
            if isinstance(json_receipt, list):
                # print(type(json_receipt))
                # print("json is list")
                self.convert_batch_json_to_text(json_receipt)
            else:
                # print("single receipt")
                self.convert_json_to_text(json_receipt)
        except Exception as e:
            self.ids.converted_json.text = str(e)
            pass

    def act(self, uri, btn=None):
        self.ids.converted_json.text = ""
        if ".json" in uri:
            # print("FOUND JSON")
            self.read_json(uri)
            if btn != None:
                btn.background_color = "blue"
        else:
            for dir_button in self.dir_buttons:
                self.ids.main_layout.remove_widget(dir_button)
            self.dir_buttons.clear()
            try:
                dir_list = sorted(os.listdir(uri))
                # print(dir_list)
                for _ in range(len(dir_list)):
                    full_path = uri + os.sep + dir_list[_]
                    # print(full_path)
                    self.dir_buttons.append(Button(text=dir_list[_], size_hint=(1, None), height="40dp",
                                                   split_str="True", text_size=(Window.width - dp(20), None),
                                                   on_press=partial(self.act, full_path)))
                    self.ids.main_layout.add_widget(self.dir_buttons[_])
                self.ids.text_input.text = uri
                # for dir_button in self.dir_buttons:
                #     dir_button.bind(on_press=partial(self.json_receipt_to_text, uri + "\\" + dir_button.text))
                #     self.ids.main_layout.add_widget(dir_button)
            except Exception as e:
                self.ids.converted_json.text = str(e)
                pass


class JsonReceiptConverterApp(App):
    pass
    # def build(self):
    #     activity = PythonActivity.mActivity
    #     intent = activity.getIntent()
    #     intent_data = intent.getData()
    #     try:
    #         uri = intent_data.toString()
    #         MainWidget.read_json(uri)
    #     except Exception as e:
    #         MainWidget.ids.converted_json.text = str(e)
    #         pass


JsonReceiptConverterApp().run()





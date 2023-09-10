from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DataWidget(BoxLayout):
    def __init__(self, data, **kwargs):
        super(DataWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        for key, value in data.items():
            label_key = Label(text=key)
            label_value = Label(text=value)
            self.add_widget(label_key)
            self.add_widget(label_value)

class DynamicLabelsApp(App):
    def build(self):
        # 数据字典定义在init函数中
        data = {
            "Name 1": "Description 1",
            "Name 2": "Description 2",
            "Name 3": "Description 3",
            "Name 4": "Description 4"
        }

        root_widget = DataWidget(data)
        return root_widget

if __name__ == '__main__':
    DynamicLabelsApp().run()







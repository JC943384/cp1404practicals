from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        data = {
            "Name 1": "Description 1",
            "Name 2": "Description 2",
            "Name 3": "Description 3",
            "Name 4": "Description 4"
        }

        root_layout = BoxLayout(orientation='vertical')

        for key, value in data.items():
            label_key = Label(text=key)
            label_value = Label(text=value)
            root_layout.add_widget(label_key)
            root_layout.add_widget(label_value)

        return root_layout


if __name__ == '__main__':
    DynamicLabelsApp().run()



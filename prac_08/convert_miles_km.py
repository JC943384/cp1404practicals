"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
JiahaoSong, IT@JCU
25/03/2024  URL:https://github.com/JC943384/cp1404practicals/tree/master/prac_08
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_text = StringProperty('')
    input_miles_value = NumericProperty(0)

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def handle_calculate(self):

        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()

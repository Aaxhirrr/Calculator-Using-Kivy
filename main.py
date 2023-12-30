from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.operator = ''
        self.last_was_operator = None
        self.result_input = TextInput(font_size=32, halign='right', readonly=True, multiline=False)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result_input)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '.', '+'],
            ['<-', '(', ')', '=']
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                if label == '=':
                    button.background_color = (0.3, 0.6, 0.3, 1)  # Change the color of '=' button
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        return layout

    def on_button_press(self, instance):
        current_input = self.result_input.text

        if instance.text == 'C':
            self.result_input.text = ''
            self.operator = ''
            self.last_was_operator = False
        elif instance.text in '+-*/':
            if current_input and not self.last_was_operator:
                self.result_input.text += instance.text
                self.operator = instance.text
                self.last_was_operator = True
        elif instance.text == '=':
            try:
                result = str(eval(current_input))
                self.result_input.text = result
            except Exception as e:
                self.result_input.text = 'Error'
        elif instance.text == '<-':
            # Backspace button
            self.result_input.text = current_input[:-1]
            self.last_was_operator = False
        elif instance.text == '.':
            # Decimal point button
            if not self.last_was_operator and '.' not in current_input:
                self.result_input.text += instance.text
                self.last_was_operator = False
        else:
            if self.last_was_operator:
                self.result_input.text += instance.text
                self.last_was_operator = False
            else:
                self.result_input.text = current_input + instance.text


if __name__ == '__main__':
    CalculatorApp().run()

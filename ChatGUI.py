from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from RetrievalChatbot import RetrievalChatbot

class BackspaceTextInput(TextInput):
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] == 'backspace':
            self.delete_selection()
            if self.cursor_index() > 0:
                self._delete_char(self.cursor_index() - 1)
        else:
            super(BackspaceTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)


class ChatGUI(App):
    def __init__(self, **kwargs):
        super(ChatGUI, self).__init__(**kwargs)
        self.bot = RetrievalChatbot("scripts/marvel.txt")

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Output field (scrollable)
        self.output_label = Label(text="", markup=True, valign='top', size_hint_y=None, height=Window.height)
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 100))
        scroll_view.add_widget(self.output_label)
        layout.add_widget(scroll_view)

        # Input field
        input_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=60)
        self.input_text = TextInput(multiline=False, size_hint=(0.8, None), height=40, background_color=(0.9, 0.9, 0.9, 1))
        self.input_text.bind(on_text_validate=self.send_message)
        input_layout.add_widget(self.input_text)
        send_button = Button(text="Send", size_hint=(0.2, None), height=40, background_normal='', background_color=(0.2, 0.6, 1, 1))
        send_button.bind(on_press=self.send_message)
        input_layout.add_widget(send_button)
        layout.add_widget(input_layout)

        return layout

    def send_message(self, instance):
        user_input = self.input_text.text
        response = self.bot.get_response(user_input)
        self.output_label.text += f"\n\n[color=3399ff]You:[/color] {user_input}\n[color=ff9933]Bot:[/color] {response}"
        self.input_text.text = ""  # Clear input field after sending
        Clock.schedule_once(self.focus_input_field, 0.1)  # Keep focus on input field

    def focus_input_field(self, dt):
        self.input_text.focus = True  # Set focus on input field

if __name__ == "__main__":
    Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Set window background color to black
    ChatGUI().run()

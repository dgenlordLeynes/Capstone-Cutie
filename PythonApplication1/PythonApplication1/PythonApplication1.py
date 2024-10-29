from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

Window.size = (400, 700)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.header_image = Image(
            source='e:/UIcutie/baybayin.png',
            size_hint=(None, None),
            size=(70, 70),
            pos_hint={'center_x': 0.5, 'top': 0.70}
        )
        self.add_widget(self.header_image)

        self.text1 = Label(
            text='Dialecto',
            font_size='25sp',
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=50,
            pos_hint={'center_x': 0.5, 'top': 0.65},
            font_name='e:/UIcutie/FONTS/Poppins-ExtraBold.ttf'
        )
        self.add_widget(self.text1)

        self.text2 = Label(
            text='Traversing Filipino Dialects',
            font_size='14sp',
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=30,
            pos_hint={'center_x': 0.5, 'top': 0.59},
            font_name='e:/UIcutie/FONTS/Poppins-Medium.ttf'
        )
        self.add_widget(self.text2)

        self.button = Button(
            text='Continue',
            font_size='12sp',
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='e:/UIcutie/FONTS/Poppins-Regular.ttf'
        )
        self.button.bind(on_press=self.go_to_second_screen)
        self.add_widget(self.button)

        self.footer = FloatLayout(size_hint_y=None, height=60, pos_hint={'center_x': 0.5, 'bottom': 0})
        self.add_widget(self.footer)

        self.background_image = Image(
            source='e:/UIcutie/background.png',
            allow_stretch=True,
            size_hint=(1, None),
            height=600,
            pos_hint={'center_x': 0.5, 'center_y': 2.0}
        )
        self.footer.add_widget(self.background_image)

        self.foreground_image = Image(
            source='e:/UIcutie/flag.png',
            allow_stretch=True,
            size_hint=(5, 5),
            pos_hint={'center_x': 0.5, 'center_y': 1.5}
        )
        self.footer.add_widget(self.foreground_image)

    def go_to_second_screen(self, instance):
        self.manager.current = 'second'

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = FloatLayout()

        label = Label(
            text='Dialecto',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            font_name='e:/UIcutie/FONTS/Poppins-ExtraBold.ttf',
            color=(0.2, 0.2, 0.2, 1),
            font_size='24sp'
        )
        layout.add_widget(label)


        with layout.canvas.before:
            Color(1, 1, 1, 1)
            button_height = 0.5 * self.height
            self.white_box = Rectangle(size=(3.39 * self.width, button_height + 0.1 * self.height), pos=(0.3 * self.width, 4.95 * self.height))

        button_layout = FloatLayout(size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.75})

        button1 = Button(
            text='Bikol',
            size_hint=(0.4, 0.3),
            font_size='15sp',
            pos_hint={'right': 1.0, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='e:/UIcutie/FONTS/Poppins-Regular.ttf'
        )
        button_layout.add_widget(button1)

        icon_image = Image(
            source='e:/UIcutie/switch.png',
            size_hint=(0.15, 0.15),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        button_layout.add_widget(icon_image)

        circle_button = Button(
            size_hint=(0.4, 0.3),
            size=(20, 20),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(1, 1, 1, 0) 
        )

        circle_button.bind(on_press=lambda x: print("Circle button pressed!"))

        def swap_button_texts(instance):
            temp_text = button1.text
            button1.text = button2.text
            button2.text = temp_text

            temp_input_text = self.text_input1.text
            self.text_input1.text = self.text_input2.text
            self.text_input2.text = temp_input_text

        circle_button.bind(on_press=swap_button_texts)

        button_layout.add_widget(circle_button)

        button2 = Button(
            text='Tagalog',
            size_hint=(0.4, 0.3),
            font_size='15sp',
            pos_hint={'right': 0.4, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='e:/UIcutie/FONTS/Poppins-Regular.ttf'
        )
        button_layout.add_widget(button2)

        layout.add_widget(button_layout)

        back_button = Button(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.5, 'y': 0.04},
            background_color=(1, 1, 1, 0)
        )

        with back_button.canvas.before:
            Color(0.2, 0.2, 0.2, 1)
            back_button.circle = Ellipse(pos=(back_button.x, back_button.y), size=(back_button.height, back_button.height))

        def update_circle(instance, value):
            back_button.circle.pos = (instance.x, instance.y)
            back_button.circle.size = (instance.height, instance.height)

        back_button.bind(size=update_circle, pos=update_circle)
        back_button.bind(on_press=self.go_to_main_screen)
        layout.add_widget(back_button)

        # TextInput for user input
        self.text_input1 = TextInput(
            hint_text='Enter your text here...',
            size_hint=(0.8, 0.2),
            font_name='e:/UIcutie/FONTS/Poppins-Regular.ttf',
            pos_hint={'center_x': 0.5, 'center_y': 0.57},
            multiline=False
        )
        self.text_input1.bind(on_text_validate=self.update_textbox2)  # Bind Enter key event
        layout.add_widget(self.text_input1)

        # TextInput for displaying content from TextInput1
        self.text_input2 = TextInput(
            hint_text='Your input will be here...',
            size_hint=(0.8, 0.2),
            font_name='e:/UIcutie/FONTS/Poppins-Regular.ttf',
            pos_hint={'center_x': 0.5, 'center_y': 0.33},
            multiline=True,
            readonly=True,  # Make it read-only
            background_color=(1, 1, 1, 1)  # Keep it visually the same as input
        )
        layout.add_widget(self.text_input2)

        # Add the main layout to the screen
        self.add_widget(layout)

    def update_textbox2(self, instance):
        self.text_input2.text = 'Marhay na aga. Anong pangaran mo? Kaogmahan kong makabisto ka. Namomotan ta ka!'
        self.text_input1.text = 'Magandang umaga. Anong pangalan mo? Natutuwa akong makilala ka. Mahal kita!'
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_to_main_screen(self, instance):
        self.manager.current = 'main'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        return sm


if __name__ == '__main__':
    MyApp().run()
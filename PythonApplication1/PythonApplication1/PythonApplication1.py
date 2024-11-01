from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.core.image import Image as CoreImage



Window.size = (400, 700)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.header_image = Image(
            source='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/baybayin.png',
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
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-ExtraBold.ttf'
        )
        self.add_widget(self.text1)

        self.text2 = Label(
            text='Traversing Filipino Dialects',
            font_size='14sp',
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=30,
            pos_hint={'center_x': 0.5, 'top': 0.59},
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Medium.ttf'
        )
        self.add_widget(self.text2)

        self.button = Button(
            text='Continue',
            font_size='12sp',
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf'
        )
        self.button.bind(on_press=self.go_to_second_screen)
        self.add_widget(self.button)

        self.footer = FloatLayout(size_hint_y=None, height=60, pos_hint={'center_x': 0.5, 'bottom': 0})
        self.add_widget(self.footer)

        self.background_image = Image(
            source='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/background.png',
            allow_stretch=True,
            size_hint=(1, None),
            height=600,
            pos_hint={'center_x': 0.5, 'center_y': 2.0}
        )
        self.footer.add_widget(self.background_image)

        self.foreground_image = Image(
            source='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/flag.png',
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
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-ExtraBold.ttf',
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
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf'
        )
        button_layout.add_widget(button1)

        icon_image = Image(
            source='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/switch.png',
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
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf'
        )
        button_layout.add_widget(button2)

        layout.add_widget(button_layout)

        bottom_button_layout = FloatLayout(size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0.02})

        square_button1 = Button(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.25, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1)
        )
        square_button1.bind(on_press=self.go_to_fourth_screen)
        bottom_button_layout.add_widget(square_button1)

        square_button2 = Button(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1)
        )
        square_button2.bind(on_press=lambda x: print("Square button 2 pressed!"))
        bottom_button_layout.add_widget(square_button2)

        square_button3 = Button(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.75, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1)
        )
        square_button3.bind(on_press=self.go_to_third_screen)
        bottom_button_layout.add_widget(square_button3)

        layout.add_widget(bottom_button_layout)

        self.text_input1 = TextInput(
            hint_text='Enter your text here...',
            size_hint=(0.8, 0.2),
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf',
            pos_hint={'center_x': 0.5, 'center_y': 0.57},
            multiline=False
        )
        self.text_input1.bind(on_text_validate=self.update_textbox2)  
        layout.add_widget(self.text_input1)

        self.text_input2 = TextInput(
            hint_text='Your input will be here...',
            size_hint=(0.8, 0.2),
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf',
            pos_hint={'center_x': 0.5, 'center_y': 0.33},
            multiline=True,
            readonly=True, 
            background_color=(1, 1, 1, 1) 
        )
        layout.add_widget(self.text_input2)

        self.add_widget(layout)

    def update_textbox2(self, instance):
        self.text_input2.text = '[Testing]Marhay na aga. Anong pangaran mo? Kaogmahan kong makabisto ka. Namomotan ta ka!'
        self.text_input1.text = '[Testing]Magandang umaga. Anong pangalan mo? Natutuwa akong makilala ka. Mahal kita!'

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_to_fourth_screen(self, instance):
        self.manager.current = 'fourth'

    def go_to_third_screen(self, instance):
        self.manager.current = 'third'

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        # Create a FloatLayout to hold the label and buttons
        layout = FloatLayout()

        # Create the label
        label = Label(
            text='Dialecto',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-ExtraBold.ttf',
            color=(0.2, 0.2, 0.2, 1),
            font_size='24sp'
        )
        layout.add_widget(label)

        # Create the white box
        with self.canvas:
            Color(1, 1, 1, 1)
            self.white_box = Rectangle(size=(self.width * 0.8, self.height * 0.6),
                                       pos=(self.center_x - (self.width * 0.8) / 2, 
                                            self.center_y - (self.height * 0.6) / 2))

        # Create button layout
        button_layout = FloatLayout(size_hint=(0.8, 0.6),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.5})

        def create_button_with_subtext(main_text, sub_text, pos_hint, icon_source):
            box = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(250, 100), spacing=10)
            
            icon = Image(source=icon_source, size_hint=(None, None), size=(40, 40), allow_stretch=True, keep_ratio=True)
            icon.size_hint_y = 0.6
            
            text_box = BoxLayout(orientation='vertical', size_hint=(1, None), spacing=2)

            button = Button(
                text=main_text,
                color=(0, 0, 0, 1),
                background_color=(1, 1, 1, 0),
                font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Medium.ttf',
                size_hint=(1, None),
                height=40
            )
            sub_label = Label(
                text=sub_text,
                color=(0.5, 0.5, 0.5, 1),
                font_size='10sp',
                size_hint=(1, None),
                height=20
            )
            
            text_box.add_widget(button)
            text_box.add_widget(sub_label)
    
            box.add_widget(icon)
            box.add_widget(text_box)
            box.pos_hint = pos_hint
            return box

        # Add buttons to the button layout
        button1 = create_button_with_subtext(
            'Offline Mode', 
            'Download the dialect and translate\ntext without using internet.', 
            {'center_x': 0.5, 'center_y': 0.85},
            'C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/offline.png'
        )
        button_layout.add_widget(button1)

        button2 = create_button_with_subtext(
            'Feedback', 
            'Share app problems and\nsuggestions with us.', 
            {'center_x': 0.5, 'center_y': 0.65},
            'C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/feedback.png'
        )
        button_layout.add_widget(button2)

        button3 = create_button_with_subtext(
            'Contact Us', 
            'Email us at\ndialectosupport@gmail.com', 
            {'center_x': 0.5, 'center_y': 0.45},
            'C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/mail.png'
        )
        button_layout.add_widget(button3)

        layout.add_widget(button_layout)

        self.add_widget(layout)

        bottom_button_layout = FloatLayout(size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0.02})

        square_button1 = Button(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.25, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1)
        )
        square_button1.bind(on_press=self.go_to_fourth_screen)
        bottom_button_layout.add_widget(square_button1)

        square_button2 = Button(
        size_hint=(None, None),
        size=(50, 50),
        pos_hint={'center_x': 0.5, 'center_y': 0.5},
        background_color=(0.2, 0.2, 0.2, 1)
        )
        square_button2.bind(on_press=self.go_to_second_screen)
        bottom_button_layout.add_widget(square_button2)

        square_button3 = Button(
        size_hint=(None, None),
        size=(50, 50),
        pos_hint={'center_x': 0.75, 'center_y': 0.5},
        background_color=(0.2, 0.2, 0.2, 1)
        )
        square_button3.bind(on_press=lambda x: print("Square button 3 pressed!"))
        bottom_button_layout.add_widget(square_button3)

        layout.add_widget(bottom_button_layout)

        inner_button = Button(
            text='About Us',
            size_hint=(None, None),
            font_size='11sp',
            size=(100, 40),
            pos_hint={'center_x': 0.5, 'y': 0.19},
            background_color=(1, 1, 1, 0), 
            color=(0, 0, 0, 1), 
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Medium.ttf'
        )
        layout.add_widget(inner_button)

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

        self.white_box.pos = (self.center_x - (self.width * 0.8) / 2, 
                              self.center_y - (self.height * 0.6) / 2)
        self.white_box.size = (self.width * 0.8, self.height * 0.6)

    def go_to_fourth_screen(self, instance):
        self.manager.current = 'fourth'

    def go_to_second_screen(self, instance):
        self.manager.current = 'second'

class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super(FourthScreen, self).__init__(**kwargs)

        # Scaling factor for the background image size
        self.bg_scale_factor = 2  # Increase to make the image appear larger

        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)  # Background color
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(1, 1, 1, 0.25)  # Set 25% opacity for the image
            bg_image = CoreImage('C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/philippines map.png')
            self.image_width, self.image_height = bg_image.size

            self.bg_image = Rectangle(
                source='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/philippines map.png',
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = FloatLayout()

        # Title (placed at the very top)
        title = Label(
            text='Dialect Challenge',
            font_size='40sp',
            pos_hint={'center_x': 0.5, 'top': 1.2},  # Positioned at the very top of the screen
            color=(0.2, 0.2, 0.2, 1),
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-ExtraBold.ttf'
        )
        layout.add_widget(title)

        # Start Playing Button (lower on the screen with more space above)
        start_button = Button(
            text='Start Playing',
            font_size='18sp',
            size_hint=(0.4, 0.08),  # Reduced size
            pos_hint={'center_x': 0.5, 'center_y': 0.2},  # Positioned lower on the screen
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf'
        )
        layout.add_widget(start_button)

        # "How to Play?" Text (lower, positioned slightly above "Start Playing" with more space)
        how_to_play_text = Label(
            text='How to Play?',
            font_size='16sp',  # Smaller font size
            pos_hint={'center_x': 0.5, 'center_y': 0.26},  # Positioned lower with more space
            color=(0.2, 0.2, 0.2, 1),
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf'
        )
        layout.add_widget(how_to_play_text)

        # Footer with the three square buttons
        bottom_button_layout = FloatLayout(size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0.02})

        square_button1 = Button(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.25, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1)
        )
        square_button1.bind(on_press=lambda x: print("Square button 1 pressed!"))
        bottom_button_layout.add_widget(square_button1)

        square_button2 = Button(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1)
        )
        square_button2.bind(on_press=self.go_to_second_screen)
        bottom_button_layout.add_widget(square_button2)

        square_button3 = Button(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.75, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1)
        )
        square_button3.bind(on_press=self.go_to_third_screen)
        bottom_button_layout.add_widget(square_button3)

        layout.add_widget(bottom_button_layout)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

        screen_width, screen_height = self.size
        aspect_ratio = self.image_width / self.image_height

        # Calculate new dimensions based on the aspect ratio and scaling factor
        if screen_width / screen_height > aspect_ratio:
            new_height = screen_height * self.bg_scale_factor
            new_width = new_height * aspect_ratio
        else:
            new_width = screen_width * self.bg_scale_factor
            new_height = new_width / aspect_ratio

        self.bg_image.size = (new_width, new_height)
        self.bg_image.pos = (
            self.center_x - new_width / 2,
            self.center_y - new_height / 2
        )

    def go_to_fourth_screen(self, instance):
        self.manager.current = 'fourth'

    def go_to_second_screen(self, instance):
        self.manager.current = 'second'

    def go_to_third_screen(self, instance):
        self.manager.current = 'third'







class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        return sm


if __name__ == '__main__':
    MyApp().run()

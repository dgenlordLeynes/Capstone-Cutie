from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.image import Image as CoreImage
from kivy.properties import ListProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.core.image import Image as CoreImage
from kivy.uix.stencilview import StencilView
from kivy.graphics import RoundedRectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior

class RoundedButton(Button):
    def __init__(self, color=(0.2, 0.2, 0.2, 1), radius=[20], **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)

        with self.canvas.before:
            Color(*color) 
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=radius)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
class CustomRoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.border = (0, 0, 0, 0)

class IconButton(ButtonBehavior, Image):
    pass


class MyWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create the bottom layout with rounded rectangle background
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1) 
            self.background_rect = RoundedRectangle(
                size=(self.width * 0.9, self.height * 0.1),  
                pos=(self.center_x - (self.width * 0.9) / 2, self.height * 0.02), 
                radius=[20]  
            )
            
Window.size = (400, 700)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.header_image = Image(
            source='assets/images/baybayin.png',
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
            font_name='assets/fonts/Poppins-ExtraBold.ttf'
        )
        self.add_widget(self.text1)

        self.text2 = Label(
            text='Traversing Filipino Dialects',
            font_size='14sp',
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=30,
            pos_hint={'center_x': 0.5, 'top': 0.59},
            font_name='assets/fonts/Poppins-Medium.ttf'
        )
        self.add_widget(self.text2)

        self.button = RoundedButton(
            text='Continue',
            font_size='12sp',
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='assets/fonts/Poppins-Regular.ttf'
        )
        self.button.bind(on_press=self.go_to_second_screen)
        self.add_widget(self.button)

        self.footer = FloatLayout(size_hint_y=None, height=60, pos_hint={'center_x': 0.5, 'bottom': 0})
        self.add_widget(self.footer)

        self.background_image = Image(
            source='assets/images/background.png',
            allow_stretch=True,
            size_hint=(1, None),
            height=600,
            pos_hint={'center_x': 0.5, 'center_y': 2.0}
        )
        self.footer.add_widget(self.background_image)

        self.foreground_image = Image(
            source='assets/images/flag.png',
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

          # Main layout for the entire screen
        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Main layout
        layout = FloatLayout()

        # Top Title and Back Button Layout
        top_layout = FloatLayout(size_hint=(1, 0.1), pos_hint={'top': 1})

        # Back button to return to MainScreen
        back_button = IconButton(
            source='assets/images/back.png',
            size_hint=(0.1, 0.5),
            pos_hint={'x': 0.02, 'center_y': 0.5}
        )
        back_button.bind(on_release=self.go_to_main_screen)
        top_layout.add_widget(back_button)

        # Title label 
        title_label = Label(
            text='Dialecto',
            font_name='assets/fonts/Poppins-ExtraBold.ttf',
            color=(0.2, 0.2, 0.2, 1),
            font_size='24sp',
            size_hint=(0.5, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        top_layout.add_widget(title_label)

        # Add top layout to main layout
        layout.add_widget(top_layout)

        # Add white box for buttons
        with layout.canvas.before:
            Color(1, 1, 1, 1)  # White color
            button_height = 0.5 * self.height
            self.white_box = RoundedRectangle(size=(3.39 * self.width, button_height + 0.1 * self.height), pos=(0.3 * self.width, 4.95 * self.height))

        # Button layout
        button_layout = FloatLayout(size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.75})

        # Button 1 (Bikol)
        button1 = RoundedButton(
            text='Bikol',
            size_hint=(0.4, 0.3),
            font_size='15sp',
            pos_hint={'right': 1.0, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='assets/fonts/Poppins-Regular.ttf',
            radius=[15]
        )
        button_layout.add_widget(button1)

        # Icon image
        icon_image = Image(
            source='assets/images/switch.png',
            size_hint=(0.15, 0.15),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        button_layout.add_widget(icon_image)

        # Circle button
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

        # Button 2 (Tagalog)
        button2 = RoundedButton(
            text='Tagalog',
            size_hint=(0.4, 0.3),
            font_size='15sp',
            pos_hint={'right': 0.4, 'center_y': 0.5},
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='assets/fonts/Poppins-Regular.ttf',
            radius=[15]
        )
        button_layout.add_widget(button2)

        layout.add_widget(button_layout)

        with layout.canvas.before:
            Color(1, 1, 1, 1)
            bottom_rect_height = 0.1 * self.height
            self.bottom_rect = RoundedRectangle(
                size=(self.width, bottom_rect_height),
                pos=(0, 0)  # Bottom left corner
            )

        # Bind size and position to update when the screen is resized
        layout.bind(size=self._update_bottom_rect, pos=self._update_bottom_rect)

        # Bottom button layout (inside the rectangle)
        bottom_button_layout = FloatLayout(size_hint=(1, 0.1), pos_hint={'y': 0.02})

        square_button1 = RoundedButton(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.25, 'center_y': 0.3},
            background_color=(0.2, 0.2, 0.2, 1),
            radius=[100]
        )
        square_button1.bind(on_press=self.go_to_fourth_screen)
        bottom_button_layout.add_widget(square_button1)

        square_button2 = RoundedButton(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0.2, 0.2, 0.2, 1),
            radius=[100]
        )
        square_button2.bind(on_press=lambda x: print("Square button 2 pressed!"))
        bottom_button_layout.add_widget(square_button2)

        square_button3 = RoundedButton(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.75, 'center_y': 0.3},
            background_color=(0.2, 0.2, 0.2, 1),
            radius=[100]
        )
        square_button3.bind(on_press=self.go_to_third_screen)
        bottom_button_layout.add_widget(square_button3)

        layout.add_widget(bottom_button_layout)

      # Text input 1
        self.text_input1 = TextInput(
            hint_text='Enter your text here...',  # Standard hint text (only visible in KivyMD or with custom behavior)
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.57},
            multiline=False,  # Single-line input
            background_color=(1, 1, 1, 1),  # White background for the text input
            foreground_color=(0, 0, 0, 1),  # Black text color
            font_name='assets/fonts/Poppins-Regular.ttf'  # Optional, use default system font if not available
        )
        layout.add_widget(self.text_input1)

# Text input 2
        self.text_input2 = TextInput(
            hint_text='Your input will be here...',  # Standard hint text
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.33},
            multiline=True,  # Multi-line input
            readonly=True,  # Makes the text input read-only
            background_color=(1, 1, 1, 1),  # White background
            foreground_color=(0, 0, 0, 1),  # Black text color
            font_name='assets/fonts/Poppins-Regular.ttf'  # Optional
        )
        layout.add_widget(self.text_input2)


          # Translate Button
        translate_button = RoundedButton(
            text='Translate',
            size_hint=(0.2, 0.05),
            font_size='12sp',
            pos_hint={'center_x': 0.5, 'center_y': 0.17},
            background_color=(0.2, 0.6, 0.8, 1),  
            radius=[15]  
        )
        translate_button.bind(on_press=self.on_translate)
        layout.add_widget(translate_button)

        # Add the main layout to the screen
        self.add_widget(layout)

    # Handling the Translate Button's Logic
    def on_translate(self, instance):  
        source_text = self.text_input1.text.strip()
        if not source_text:
            self.text_input2.text = "Please enter some text to translate!"
        else:
            # Replace with actual translation logic
            translated_text = f"Translated: {source_text}"
            self.text_input2.text = translated_text

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_to_main_screen(self, instance):
        self.manager.current = 'main'

    def go_to_fourth_screen(self, instance):
        self.manager.current = 'fourth'

    def go_to_third_screen(self, instance):
        self.manager.current = 'third'

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def _update_bottom_rect(self, instance, value):
        # Update bottom button background rectangle when the screen resizes
        self.bottom_rect.pos = (0, 0)  # Bottom left corner
        self.bottom_rect.size = (self.width, 0.1 * self.height)  # Adjust height relative to screen size
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
            font_name='assets/fonts/Poppins-ExtraBold.ttf',
            color=(0.2, 0.2, 0.2, 1),
            font_size='24sp'
        )
        layout.add_widget(label)

        # Create the white box
        with self.canvas:
            Color(1, 1, 1, 1)
            self.white_box = RoundedRectangle(size=(self.width * 0.8, self.height * 0.6),
                                       pos=(self.center_x - (self.width * 0.8) / 2, 
                                            self.center_y - (self.height * 0.6) / 2))

        # Create button layout
        button_layout = FloatLayout(size_hint=(0.8, 0.6),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.5})

        def create_button_with_subtext(main_text, sub_text, pos_hint, icon_source):
            box = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(250, 100), spacing=10,)
            
            icon = Image(source=icon_source, size_hint=(None, None), size=(40, 40), allow_stretch=True, keep_ratio=True)
            icon.size_hint_y = 0.6
            
            text_box = BoxLayout(orientation='vertical', size_hint=(1, None), spacing=2)

            button = Button(
                text=main_text,
                color=(0, 0, 0, 1),
                background_color=(1, 1, 1, 0),
                font_name='assets/fonts/Poppins-Medium.ttf',
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
            'assets/images/offline.png'
        )
        button_layout.add_widget(button1)

        button2 = create_button_with_subtext(
            'Feedback', 
            'Share app problems and\nsuggestions with us.', 
            {'center_x': 0.5, 'center_y': 0.65},
            'assets/images/feedback.png'
        )
        button_layout.add_widget(button2)

        button3 = create_button_with_subtext(
            'Contact Us', 
            'Email us at\ndialectosupport@gmail.com', 
            {'center_x': 0.5, 'center_y': 0.45},
            'assets/images/mail.png'
        )
        button_layout.add_widget(button3)

        layout.add_widget(button_layout)

        self.add_widget(layout)

        with layout.canvas.before:
            Color(1, 1, 1, 1)
            bottom_rect_height = 0.1 * self.height
            self.bottom_rect = RoundedRectangle(
                size=(self.width, bottom_rect_height),
                pos=(0, 0)  # Bottom left corner
            )

        # Bind size and position to update when the screen is resized
        layout.bind(size=self._update_bottom_rect, pos=self._update_bottom_rect)

        # Bottom button layout (inside the rectangle)
        bottom_button_layout = FloatLayout(size_hint=(1, 0.1), pos_hint={'y': 0.02})

        square_button1 = RoundedButton(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.25, 'center_y': 0.3},
            background_color=(0.2, 0.2, 0.2, 1),
            radius=[100]
        )
        square_button1.bind(on_press=self.go_to_fourth_screen)
        bottom_button_layout.add_widget(square_button1)

        square_button2 = RoundedButton(
        size_hint=(None, None),
        size=(50, 50),
        pos_hint={'center_x': 0.5, 'center_y': 0.3},
        background_color=(0.2, 0.2, 0.2, 1),
        radius=[100]
        )
        square_button2.bind(on_press=self.go_to_second_screen)
        bottom_button_layout.add_widget(square_button2)

        square_button3 = RoundedButton(
        size_hint=(None, None),
        size=(50, 50),
        pos_hint={'center_x': 0.75, 'center_y': 0.3},
        background_color=(0.2, 0.2, 0.2, 1),
        radius=[100]
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
            font_name='assets/fonts/Poppins-Medium.ttf'
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

    def _update_bottom_rect(self, instance, value):
        # Update bottom button background rectangle when the screen resizes
        self.bottom_rect.pos = (0, 0)  
        self.bottom_rect.size = (self.width, 0.1 * self.height)  # Adjust height relative to screen size

class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super(FourthScreen, self).__init__(**kwargs)

        self.bg_scale_factor = 2 

        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)  
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(1, 1, 1, 0.25)  
            bg_image = CoreImage('assets/images/philippines map.png')
            self.image_width, self.image_height = bg_image.size

            self.bg_image = Rectangle(
                source='assets/images/philippines map.png',
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = FloatLayout()

        # Title 
        title = Label(
            text='Dialect Challenge',
            font_size='40sp',
            pos_hint={'center_x': 0.5, 'top': 1.2}, 
            color=(0.2, 0.2, 0.2, 1),
            font_name='assets/fonts/Poppins-ExtraBold.ttf'
        )
        layout.add_widget(title)

        # Start Playing Button 
        start_button = RoundedButton(
            text='Start Playing',
            font_size='18sp',
            size_hint=(0.4, 0.08),  
            pos_hint={'center_x': 0.5, 'center_y': 0.2},  
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='assets/fonts/Poppins-Regular.ttf',
            radius=[10]
        )
        start_button.bind(on_press=self.go_to_fifth_screen)
        layout.add_widget(start_button)

        # "How to Play?" Text 
        how_to_play_text = Label(
            text='How to Play?',
            font_size='16sp',  
            pos_hint={'center_x': 0.5, 'center_y': 0.26}, 
            color=(0.2, 0.2, 0.2, 1),
            font_name='assets/fonts/Poppins-Regular.ttf'
        )
        layout.add_widget(how_to_play_text)

        with layout.canvas.before:
            Color(1, 1, 1, 1)
            bottom_rect_height = 0.1 * self.height
            self.bottom_rect = RoundedRectangle(
                size=(self.width, bottom_rect_height),
                pos=(0, 0)  
            )

        # Bind size and position to update when the screen is resized
        layout.bind(size=self._update_bottom_rect, pos=self._update_bottom_rect)

        # Bottom button layout (inside the rectangle)
        bottom_button_layout = FloatLayout(size_hint=(1, 0.1), pos_hint={'y': 0.02})

        square_button1 = RoundedButton(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.25, 'center_y': 0.3},
            background_color=(0.2, 0.2, 0.2, 1),
            radius=[100]
        )
        square_button1.bind(on_press=lambda x: print("Square button 1 pressed!"))
        bottom_button_layout.add_widget(square_button1)

        square_button2 = RoundedButton(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0.2, 0.2, 0.2, 1),
            radius=[100]
        )
        square_button2.bind(on_press=self.go_to_second_screen)
        bottom_button_layout.add_widget(square_button2)

        square_button3 = RoundedButton(
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.75, 'center_y': 0.3},
            background_color=(0.2, 0.2, 0.2, 1),
            radius=[100]
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

    def go_to_fifth_screen(self, instance):
        self.manager.current = 'fifth'

    def _update_bottom_rect(self, instance, value):
        self.bottom_rect.pos = (0, 0)  
        self.bottom_rect.size = (self.width, 0.1 * self.height)  

class FifthScreen(Screen):
    def __init__(self, **kwargs):
        super(FifthScreen, self).__init__(**kwargs)

        # Set yellow background as the base layer
        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)  # Yellow background color
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

            # White circle (background image)
            try:
                self.bg_image = CoreImage('assets/images/white circle.png').texture
                Color(1, 1, 1, 1)  # Reset to white (for clarity)
                self.bg_image_rect = Rectangle(texture=self.bg_image, size=self.size, pos=self.pos)
            except Exception as e:
                print(f"Error loading background image: {e}")
                self.bg_image_rect = None

            # White rectangle for the `magayon` label
            Color(1, 1, 1, 1)  # White color
            self.word_bg_rect = RoundedRectangle(size=(200, 80), pos=(self.center_x - 100, self.height * 0.65))

        # Bind size and position updates for background
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Main layout
        self.layout = FloatLayout()
        self.add_widget(self.layout)

        # --- Top bar with progress and score ---
        top_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), pos_hint={'top': 1})

        # Back button
        back_button = RoundedButton(
            text='Back', size_hint=(None, None), size=(100, 50),
            pos_hint={'x': 1000, 'top': 0.15}, font_size='20sp',
            background_normal='', background_color=(0.2, 0.2, 0.2, 0.5)
        )
        back_button.bind(on_press=self.go_back)

        # Progress label
        self.progress = Label(
            text='2/10', font_size='20sp', color=(0, 0, 0, 1),
            pos_hint={'center_x': 0.5, 'top': 0.3}
        )

        # Score layout
        self.score_layout = BoxLayout(
            orientation='vertical', size_hint=(None, None), size=(100, 60),
            pos_hint={'right': 1, 'top': 0.25}
        )
        self.score_text = Label(text='Score:', font_size='12sp', color=(0, 0, 0, 1), size_hint=(1, None), height=20)
        self.score_value = Label(text='87', font_size='24sp', color=(0, 0, 0, 1), size_hint=(1, None), height=40)
        self.score_layout.add_widget(self.score_text)
        self.score_layout.add_widget(self.score_value)

        # Add components to the top bar
        top_bar.add_widget(back_button)
        top_bar.add_widget(self.progress)
        top_bar.add_widget(self.score_layout)
        self.layout.add_widget(top_bar)

        # --- Word Label ---
        self.word_label = Label(
            text='magayon', font_size='30sp', color=(0.2, 0.2, 0.2, 1),
            size_hint=(None, None), size=(200, 80), halign='center', valign='middle'
        )
        self.word_label.bind(size=self.word_label.setter('text_size'))
        self.word_label.pos_hint = {'center_x': 0.5, 'center_y': 0.70}
        self.layout.add_widget(self.word_label)

        # --- Answer Choices ---
        self.answer_layout = BoxLayout(
            orientation='vertical', size_hint=(0.8, None), height=150, spacing=10,
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        answer_texts = ['magaling', 'masama', 'maganda']
        for text in answer_texts:
            answer_button = RoundedButton(
                text=text, font_size='20sp', background_normal='', background_color=(1, 1, 1, 1),
                color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height=40, radius=[10]
            )
            self.answer_layout.add_widget(answer_button)
        self.layout.add_widget(self.answer_layout)

        # --- Done Button ---
        self.done_button = RoundedButton(
            text='Done', size_hint=(None, None), size=(300, 40), pos_hint={'center_x': 0.5, 'y': 0.1},
            font_size='18sp', background_normal='', background_color=(0.2, 0.2, 0.2, 1)
        )
        self.done_button.bind(on_press=self.go_to_end_challenge)
        self.layout.add_widget(self.done_button)

    # --- Transition to End Challenge ---
    def go_to_end_challenge(self, instance):
        end_screen = self.manager.get_screen('end_challenge')
        end_screen.score_label.text = f"Your score: {self.score_value.text}"  # Pass score dynamically
        self.manager.current = 'end_challenge'

    # --- Back Navigation ---
    def go_back(self, instance):
        self.manager.current = 'fourth'

    # --- Update Background Rectangles ---
    def _update_rect(self, instance, value):
    # Update yellow background rectangle
        if hasattr(self, 'bg_rect'):
            self.bg_rect.size = self.size
            self.bg_rect.pos = self.pos

    # Update the background image rectangle (white circle)
        if hasattr(self, 'bg_image_rect') and self.bg_image_rect:
        # Increase the size of the circle to cover more area
            circle_scale = 1  # Increase the scale factor to make the circle larger
            self.bg_image_rect.size = (self.width * circle_scale, self.height * circle_scale)
            self.bg_image_rect.pos = (
            self.center_x - self.bg_image_rect.size[0] / 2,  # Center horizontally
            self.center_y - self.bg_image_rect.size[1] / 2  # Center vertically (adjust if necessary)
        )

    # Update the word label's background rectangle
        if hasattr(self, 'word_bg_rect'):
            self.word_bg_rect.size = (self.word_label.width + 20, self.word_label.height + 20)
            self.word_bg_rect.pos = (self.word_label.x - 10, self.word_label.y - 10)

class EndChallengeScreen(Screen):
    def __init__(self, **kwargs):
        super(EndChallengeScreen, self).__init__(**kwargs)

        self.bg_scale_factor = 2 

        # Background setup with image (Philippines map)
        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)  # Light yellow background
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
            
            # Load the background map image
            Color(1, 1, 1, 0.25)  
            self.bg_image = CoreImage('assets/images/philippines map.png')
            self.bg_width, self.bg_height = self.bg_image.size
            
            self.bg_map = Rectangle(
                source='assets/images/philippines map.png',
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self._update_rect, pos=self._update_rect)

        # Main layout for the screen
        layout = FloatLayout()
        self.add_widget(layout)

        # Title text for "Dialect Challenge"
        title = Label(
            text='Dialect Challenge',
            font_size='40sp',
            pos_hint={'center_x': 0.5, 'top': 1.2},  # Position it above
            color=(0.2, 0.2, 0.2, 1),
            font_name='assets/fonts/Poppins-ExtraBold.ttf'
        )
        layout.add_widget(title)

        # Score label
        self.score_label = Label(
            text="Your score: 0",  # Placeholder, update with actual score
            font_size='30sp',
            color=(0.2, 0.2, 0.2, 1),
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        layout.add_widget(self.score_label)

        # Start New Game button
        self.new_game_button = RoundedButton(
            text='Start New Game',
            font_size='18sp',
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='assets/fonts/Poppins-Regular.ttf'
        )
        self.new_game_button.bind(on_press=self.start_new_game)
        layout.add_widget(self.new_game_button)

        # Share button
        self.share_button = RoundedButton(
            text='Share',
            font_size='18sp',
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='assets/fonts/Poppins-Regular.ttf'
        )
        self.share_button.bind(on_press=self.share_score)
        layout.add_widget(self.share_button)

    def start_new_game(self, instance):
        self.manager.current = 'fourth'  # Navigate to the 'fourth' screen

    def share_score(self, instance):
        print("Score shared!")  # Replace with actual share logic

    def _update_rect(self, instance, value):
        if hasattr(self, 'bg_rect'):
            self.bg_rect.size = self.size
            self.bg_rect.pos = self.pos
            self.bg_map.size = self.size
            self.bg_map.pos = self.pos



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(FifthScreen(name='fifth'))
        sm.add_widget(EndChallengeScreen(name='end_challenge'))
        return sm


if __name__ == '__main__':
    MyApp().run()

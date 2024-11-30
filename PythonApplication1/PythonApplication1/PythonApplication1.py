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

class RoundedTextInput(TextInput):
    # Properties for the radius of rounded corners and background color
    radius = ListProperty([10, 10, 10, 10])  
    background_color = ListProperty([1, 1, 1, 1])  
    def __init__(self, **kwargs):
        super(RoundedTextInput, self).__init__(**kwargs)
        self.bind(size=self.update_canvas, pos=self.update_canvas)
        
    def update_canvas(self, *args):
        # Clear the previous canvas drawing before rendering a new one
        self.canvas.before.clear()
        
        with self.canvas.before:
            from kivy.graphics import Color
            Color(*self.background_color) 
            # Draw the rounded rectangle based on the size and position of the TextInput
            self.rounded_rect = RoundedRectangle(
                size=self.size, 
                pos=self.pos, 
                radius=self.radius
            )

    def on_focus(self, instance, value):
        # Update the canvas when the input is focused or unfocused
        self.update_canvas()

    def on_focus(self, instance, value):
        # Redraw the background when the input is focused or unfocused
        self.update_canvas()

    def on_text(self, instance, value):
        # Trigger canvas update when text is entered or removed
        self.update_canvas()

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

        self.button = RoundedButton(
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
            source='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/back.png',
            size_hint=(0.1, 0.5),
            pos_hint={'x': 0.02, 'center_y': 0.5}
        )
        back_button.bind(on_release=self.go_to_main_screen)
        top_layout.add_widget(back_button)

        # Title label 
        title_label = Label(
            text='Dialecto',
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-ExtraBold.ttf',
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
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf',
            radius=[15]
        )
        button_layout.add_widget(button1)

        # Icon image
        icon_image = Image(
            source='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/switch.png',
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
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf',
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
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
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
        self.text_input1 = RoundedTextInput(
        hint_text='Enter your text here...',  # Hint text will be visible now
        size_hint=(0.8, 0.2),
        font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf',
        pos_hint={'center_x': 0.5, 'center_y': 0.57},
        multiline=False,
        background_color=(1, 1, 1, 1),  # White background for the text input
        radius=[15, 15, 15, 15]  # Rounded corners
        )
        layout.add_widget(self.text_input1)

# Text input 2
        self.text_input2 = RoundedTextInput(
        hint_text='Your input will be here...',  # Hint text will be visible now
        size_hint=(0.8, 0.2),
        font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf',
        pos_hint={'center_x': 0.5, 'center_y': 0.33},
        multiline=True,
        readonly=True,
        background_color=(1, 1, 1, 1),  # White background
        radius=[15, 15, 15, 15]  # Rounded corners
        )
        layout.add_widget(self.text_input2)
        
        self.add_widget(layout)

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
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-ExtraBold.ttf',
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
        pos_hint={'center_x': 0.75, 'center_y': 0.6},
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
            bg_image = CoreImage('C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/philippines map.png')
            self.image_width, self.image_height = bg_image.size

            self.bg_image = Rectangle(
                source='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/philippines map.png',
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
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-ExtraBold.ttf'
        )
        layout.add_widget(title)

        # Start Playing Button 
        start_button = RoundedButton(
            text='Start Playing',
            font_size='18sp',
            size_hint=(0.4, 0.08),  
            pos_hint={'center_x': 0.5, 'center_y': 0.2},  
            background_color=(0.2, 0.2, 0.2, 1),
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf',
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
            font_name='C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/FONTS/Poppins-Regular.ttf'
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
            pos_hint={'center_x': 0.25, 'center_y': 0.6},
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

        # Set background color first to ensure it is at the base layer
        with self.canvas.before:
            Color(0.976, 0.875, 0.427, 1)  
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Attempt to load the background image
        try:
            self.bg_image = CoreImage('C:/Users/Dgenlord Leynes/source/repos/Capstone-Cutie/UIcutie/white circle.png').texture
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.bg_image = None  # Fallback in case of error
        
        # If image is available, add it on top of the yellow background
        if self.bg_image:
            with self.canvas.before:
                Color(1, 1, 1, 1)  
                self.bg_image_rect = Rectangle(texture=self.bg_image, size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Main layout using FloatLayout
        self.layout = FloatLayout()
        self.add_widget(self.layout)

        # Top bar with progress and score
        top_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), pos_hint={'top': 1})

        # Back button
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 50),
                                     pos_hint={'x': 0.05, 'top': 0.15}, font_size='20sp', background_normal='', background_color=(0.2, 0.2, 0.2, 0.5))
        back_button.bind(on_press=self.go_back)

        # Progress label
        self.progress = Label(text='2/10', font_size='20sp', color=(0, 0, 0, 1), pos_hint={'center_x': 0.5, 'top': 0.3})

        # Score layout
        self.score_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 60), pos_hint={'right': 1, 'top': 0.25})
        self.score_text = Label(text='Score:', font_size='12sp', color=(0, 0, 0, 1), size_hint=(1, None), height=20)
        self.score_value = Label(text='87', font_size='24sp', color=(0, 0, 0, 1), size_hint=(1, None), height=40)
        self.score_layout.add_widget(self.score_text)
        self.score_layout.add_widget(self.score_value)

        # Add components to the top bar
        top_bar.add_widget(back_button)
        top_bar.add_widget(self.progress)
        top_bar.add_widget(self.score_layout)
        self.layout.add_widget(top_bar)

        # Initialize score_background rectangle (for the background of the score layout)
        with self.canvas.before:
            self.score_background = Rectangle(size=self.score_layout.size, pos=self.score_layout.pos)

        # Word label (restored to original rounded rectangle background)
        self.word_label = Label(text='magayon', font_size='30sp', color=(0.2, 0.2, 0.2, 1),
                                size_hint=(None, None), size=(200, 80), halign='center', valign='middle')
        self.word_label.bind(size=self.word_label.setter('text_size'))
        self.word_label.pos_hint = {'center_x': 0.5, 'center_y': 0.70}
        self.layout.add_widget(self.word_label)

        # Rounded rectangle background for the word label
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Slightly translucent background color for the word label
            self.word_background = RoundedRectangle(size=(self.word_label.width + 40, self.word_label.height + 40),
                                                    pos=(self.word_label.x - 20, self.word_label.y - 20),
                                                    radius=[15])
        
        self.bind(size=self.update_word_background, pos=self.update_word_background)

        # Answer choices (example with dummy options)
        self.answer_layout = BoxLayout(orientation='vertical', size_hint=(0.8, None), height=150, spacing=10, pos_hint={'center_x': 0.5, 'center_y': 0.4})
        answer_texts = ['magaling', 'masama', 'maganda']
        for text in answer_texts:
            answer_button = RoundedButton(text=text, font_size='20sp', background_normal='', background_color=(1, 1, 1, 1), 
                                          color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height=40, radius=[10])
            self.answer_layout.add_widget(answer_button)
        self.layout.add_widget(self.answer_layout)

        # Done button
        self.done_button = RoundedButton(text='Done', size_hint=(None, None), size=(300, 40), pos_hint={'center_x': 0.5, 'y': 0.1},
                                         font_size='18sp', background_normal='', background_color=(0.2, 0.2, 0.2, 1))
        self.layout.add_widget(self.done_button)

    def go_back(self, instance):
        self.manager.current = 'fourth'

    def _update_rect(self, instance, value):
        # Update background rectangle
        if self.bg_rect:
            self.bg_rect.pos = self.pos
            self.bg_rect.size = self.size
        if self.bg_image_rect:
            self.bg_image_rect.pos = self.pos
            self.bg_image_rect.size = self.size

    def update_word_background(self, *args):
        # Update the word background rectangle with the new size and position
        if self.word_background:
            self.word_background.size = (self.word_label.width + 40, self.word_label.height + 40)
            self.word_background.pos = (self.word_label.x - 20, self.word_label.y - 20)

    def update_score_background(self, *args):
        # Update the score layout background
        if hasattr(self, 'score_background'):
            self.score_background.size = self.score_layout.size
            self.score_background.pos = self.score_layout.pos

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(FifthScreen(name='fifth'))
        return sm


if __name__ == '__main__':
    MyApp().run()

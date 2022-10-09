from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    GridLayout:

        cols: 2
        rows: 2
        row_force_default: True
        row_default_height: 40

        Button:
            text: 'Login'
            on_press: root.manager.current = 'login'
            size_hint_x: None
            width: 100
        Button:
            text: 'Sign Up'
            on_press: root.manager.current = 'signup'
            size_hint_x: None
            width: 100

<LoginScreen>:
    GridLayout:

        cols: 2
        rows: 2
        row_force_default: True
        row_default_height: 40

        Button:
            text: 'login page'
            size_hint_x: None
            width: 100
        Button:
            text: 'Menu'
            on_press: root.manager.current = 'menu'
            size_hint_x: None
            width: 100
        TextInput
            text: 'email'
            size_hint_x: None
            width: 100
            hight: 50
        TextInput
            text: 'Password'
            size_hint_x: None
            width: 100
            hight: 50

<SignupScreen>:
    GridLayout:

        cols: 2
        rows: 2
        row_force_default: True
        row_default_height: 40

        Button:
            text: 'SignUp page'
            size_hint_x: None
            width: 100
        Button:
            text: 'Menu'
            on_press: root.manager.current = 'menu'
            size_hint_x: None
            width: 100

""")

# Declare both screens
class MenuScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))

        return sm

if __name__ == '__main__':
    TestApp().run()
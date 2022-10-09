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
            text: 'Drop off'
            on_press: root.manager.current = 'dropoff'
            size_hint_x: None
            width: 100
        Button:
            text: 'Pick up'
            on_press: root.manager.current = 'pickup'
            size_hint_x: None
            width: 100

<DropoffScreen>:
    GridLayout:

        cols: 2
        rows: 2
        row_force_default: True
        row_default_height: 40

        Button:
            text: 'Dropoff page'
            size_hint_x: None
            width: 100
        Button:
            text: 'Menu'
            on_press: root.manager.current = 'menu'
            size_hint_x: None
            width: 100
        Button:
            text: 'Scan Barcode'
            on_press: root.manager.current = 'scan'
            size_hint_x: None
            width: 100
        TextInput
            text: 'Would be scan results / manual enter section'
            size_hint_x: None
            width: 400
            hight: 50

<PickupScreen>:
    GridLayout:

        cols: 2
        rows: 2
        row_force_default: True
        row_default_height: 40

        Button:
            text: 'Pickup page'
            size_hint_x: None
            width: 100
        Button:
            text: 'Menu'
            on_press: root.manager.current = 'menu'
            size_hint_x: None
            width: 100
        Button:
            text: 'Scan Barcode'
            on_press: root.manager.current = 'scan'
            size_hint_x: None
            width: 100
        TextInput
            text: 'Would be scan results / manual enter section'
            size_hint_x: None
            width: 400
            hight: 50

<ScanScreen>:
    GridLayout:

        cols: 2
        rows: 2
        row_force_default: True
        row_default_height: 40

        Button:
            text: 'Mock scan page'
            size_hint_x: None
            width: 200
        Button:
            text: 'Menu'
            on_press: root.manager.current = 'menu'
            size_hint_x: None
            width: 100

""")

# Declare both screens
class MenuScreen(Screen):
    pass

class DropoffScreen(Screen):
    pass

class PickupScreen(Screen):
    pass

class ScanScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(DropoffScreen(name='dropoff'))
        sm.add_widget(PickupScreen(name='pickup'))
        sm.add_widget(ScanScreen(name='scan'))

        return sm

if __name__ == '__main__':
    TestApp().run()
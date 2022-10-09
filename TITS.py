from kivy.app import App
from kivy.lang import Builder
import requests
#tested requests already and this is working currently. Must be prebuilt into python so opop

#below is copied code from a open source repo. This is zbarcam example proj currently running
#we need to make this a selectable section in the app. So need to build a paging system first
#Will make diagram of app flow page layout and put in wiki.
DEMO_APP_KV_LANG = """
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
BoxLayout:
    orientation: 'vertical'
    ZBarCam:
        id: zbarcam
        # optional, by default checks all types
        code_types: 'QRCODE', 'EAN13'
    Label:
        size_hint: None, None
        size: self.texture_size[0], 50
        text: ', '.join([str(symbol.data) for symbol in zbarcam.symbols])
"""


class DemoApp(App):

    def build(self):
        return Builder.load_string(DEMO_APP_KV_LANG)


if __name__ == '__main__':
    DemoApp().run()

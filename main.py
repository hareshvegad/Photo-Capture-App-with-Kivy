from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import platform

from photoscreen1 import PhotoScreen1

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

class MyApp(App):
    
    def build(self):
        self.enable_swipe = False
        self.sm = ScreenManager()
        self.screen = PhotoScreen1(name='1')
        self.sm.add_widget(self.screen)

        return self.sm

MyApp().run()


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''
<ScreenManager>:
    HomeScreen
    AnotherScreen

<HomeScreen>:
    name: 'home'
    Button:
        text: 'Go to another screen'
        on_release: root.manager.current = 'another'

<AnotherScreen>:
    name: 'another'
    Button:
        text: "Go back home"
        on_release: root.manager.current = 'home'
''')

class ScreenManager(ScreenManager):
    pass

class HomeScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class DemoApp(App):
    def build(self):
        return ScreenManager()

DemoApp().run()
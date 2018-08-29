from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string('''
<OneScreen>
    Label:
        text: "My mother screen was created by kv and python codes."
''')

class OneScreen(Screen):
    pass

class DemoApp(App):
    def build(self):
        return OneScreen()

DemoApp().run()
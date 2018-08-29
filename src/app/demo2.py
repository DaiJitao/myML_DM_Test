from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string('''
<OneScreen>
    Button:
        text: 'Click me'
        on_release: print(root.__class__)
''')

class OneScreen(Screen):
    pass

class DemoApp(App):
    def build(self):
        return OneScreen()

DemoApp().run()
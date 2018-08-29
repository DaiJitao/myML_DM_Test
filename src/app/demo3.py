from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string('''
<OneScreen>
    BoxLayout:
        Button:
            text: 'Click me'
            on_release: root.do_something()
        Button:
            text: 'Who made this?'
            on_release: print(root.author)
''')


class OneScreen(Screen):
    def __init__(self, **kwargs):
        self.author = 'yingshaoxo'
        super(OneScreen, self).__init__(**kwargs)

    def do_something(self):
        print('2333')


class DemoApp(App):
    def build(self):
        return OneScreen()


DemoApp().run()
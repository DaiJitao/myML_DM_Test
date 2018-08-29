
from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_string(
    '''
Button:
    text: "I was created by kv codes"
'''
)

class DemoApp(App):
    def build(self):
        return kv


DemoApp().run()
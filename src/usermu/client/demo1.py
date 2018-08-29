from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from time import gmtime, strftime # this equls cv codes #...

Builder.load_string("""
#:import gmtime time.gmtime
#:import strftime time.strftime

<RootWidget>
    BoxLayout:
        orientation: 'vertical'
        Button:
            id: change_itself
            text: 'I can change myself'
            on_release: root.ids['change_itself'].text = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        Button:
            id: change_all
            text: 'I can change our behavior'
            on_release: root.change_all()
""")

class RootWidget(Screen):
    def change_all(self):
        print(self.ids)
        for instance_class in self.ids.values():
            instance_class.text = 'Exit'
            instance_class.bind(on_release=exit)

class DemoApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    DemoApp().run()
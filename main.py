from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        slider = Slider()
        button = Button(text="Go to screen 2")
        button.bind(on_press=self.switch_screen)

        layout.add_widget(slider)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_screen(self, instance):
        app = App.get_running_app()
        app.root.current = 'screen2'


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Go to Screen 1')
        switch = Switch()

        button.bind(on_press=self.switch_screen)
        layout.add_widget(switch)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_screen(self, instance):
        app = App.get_running_app()
        app.root.current = 'screen1'


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Screen1(name='screen1'))
        self.screen_manager.add_widget(Screen2(name='screen2'))
        return self.screen_manager


if __name__ == '__main__':
    MyApp().run()
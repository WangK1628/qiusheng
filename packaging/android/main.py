"""Android entrypoint for Kivy-packaged prototype.
This wraps the existing CLI game with a minimal label so APK can launch.
"""

from kivy.app import App
from kivy.uix.label import Label


class InfiniteSurvivalApp(App):
    def build(self):
        return Label(text="Infinite Survival Prototype\nAPK build successful")


if __name__ == "__main__":
    InfiniteSurvivalApp().run()

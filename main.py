from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class GeksaTacticGame(MDApp):
    def build(self):
        return MDLabel(text = "Hello, I am developer of this game",halign = "center")

GeksaTacticGame().run()
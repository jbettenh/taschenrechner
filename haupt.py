#Mein Taschenrechner mit Python und Kivy
import kivy
kivy.require("1.9.2")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class RechnerLayout(GridLayout):
    def calculate(self, rechnung):
        if rechnung:
            try:
                # Solve formula and display it in entry
                # which is pointed at by the display
                self.display.text = str(eval(rechnung))
            except Exception:
                self.display.text = "Fehler"


class RechnerKvApp(App):
    def build(self):
        return RechnerLayout()

rechApp = RechnerKvApp()
rechApp.run()
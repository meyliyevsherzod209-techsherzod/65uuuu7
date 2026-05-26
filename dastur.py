from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.label import MDLabel

class AIYordamchiApp(MDApp):
    def build(self):
        screen = MDScreen()

        # Ekrandagi matn
        self.holat_yozuvi = MDLabel(
            text="Menga buyruq bering...",
            halign="center",
            font_style="H5",
            pos_hint={"center_y": 0.6}
        )
        screen.add_widget(self.holat_yozuvi)

        # Mikrofon tugmasi
        mikrofon_tugma = MDFloatingActionButton(
            icon="microphone",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.buyruqni_boshla
        )
        screen.add_widget(mikrofon_tugma)

        return screen

    def buyruqni_boshla(self, instance):
        self.holat_yozuvi.text = "Sizni eshityapman..."

if __name__== "__main__":
    AIYordamchiApp().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import storagepath, filechooser
import os
import shutil

class CleanerApp(App):
    def clean_cache(self, instance):
        cache_dirs = [
            "/storage/emulated/0/Android/data/",
            "/storage/emulated/0/Android/obb/"
        ]
        
        deleted_files = 0
        for directory in cache_dirs:
            if os.path.exists(directory):
                for folder in os.listdir(directory):
                    folder_path = os.path.join(directory, folder, "cache")
                    if os.path.exists(folder_path):
                        try:
                            shutil.rmtree(folder_path)
                            deleted_files += 1
                        except Exception as e:
                            print(f"Erro ao deletar {folder_path}: {e}")

        instance.text = f"Cache limpo ({deleted_files} pastas)"

    def build(self):
        layout = BoxLayout(orientation="vertical")
        btn_clean = Button(text="Limpar Cache", on_press=self.clean_cache)
        layout.add_widget(btn_clean)
        return layout

if __name__ == "__main__":
    CleanerApp().run()
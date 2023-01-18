import shutil
import pyvan
import os

OPTIONS = {
    "main_file_name": "main.py",
    "show_console": False,
    "use_pipreqs": True
}

pyvan.build(**OPTIONS)

gui_folder = os.path.abspath("../../gui/")
dist_folder = os.path.abspath("./dist/gui")

shutil.copytree(gui_folder, dist_folder)

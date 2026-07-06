import subprocess
import os


class AppLauncher:

    def open_calculator(self):
        subprocess.Popen("calc.exe")

    def open_notepad(self):
        subprocess.Popen("notepad.exe")

    def open_paint(self):
        subprocess.Popen("mspaint.exe")

    def open_explorer(self):
        subprocess.Popen("explorer.exe")

    def open_cmd(self):
        subprocess.Popen("cmd.exe")

    def open_camera(self):
        os.system("start microsoft.windows.camera:")

    def open_vscode(self):
        try:
            subprocess.Popen("code")
        except:
            print("VS Code is not installed or PATH is not set.")
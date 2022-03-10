import os
import platform
import sys
from kivy.core.window import Window
from kivy.logger import LOG_LEVELS, Logger


def setup_env():
    root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
    sys.path.insert(0, os.path.join(root_dir, "libs", "utils"))
    Logger.setLevel(LOG_LEVELS["debug"])

    # This is needed for supporting Windows 10 with OpenGL < v2.0
    if platform.system() == "Windows":
        from win32api import GetSystemMetrics  # pip install pywin32 
        
        app_size = (1240, 740)
        Window.size = app_size
        Window.top = 50
        Window.left = GetSystemMetrics(0) - 50 - app_size[0] 
        os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"






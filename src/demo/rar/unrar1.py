
import os

try:
    import unrar
except:
    os.system("pip install unrar")

from unrar import rarfile
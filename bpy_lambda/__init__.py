import ctypes
import os

dir = os.path.dirname(os.path.realpath(__file__))
ctypes.cdll.LoadLibrary(os.path.join(dir, 'libGLU.so.1'))
ctypes.cdll.LoadLibrary(os.path.join(dir, 'libpython3.5m.so.1.0'))

from . import bpy

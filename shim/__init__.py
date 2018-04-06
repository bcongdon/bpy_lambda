import ctypes
import os

lib_dir = os.path.dirname(os.path.realpath(__file__))

LIBRARIES = [
    'libHalf.so.12',
    'libIex.so.12',
    'libImath.so.12',
    'libIlmThread.so.12',
    'libIlmImf.so.22',
    'libboost_system.so.1.60.0',
    'libboost_filesystem.so.1.60.0',
    'libboost_regex.so.1.60.0',
    'libboost_thread.so.1.60.0',
    'libpython3.6m.so.1.0',
    'libGLU.so.1',
    'libopenjpeg.so.2',
    'libOpenImageIO.so.1.7',
]

for lib in LIBRARIES:
    print(os.path.join(lib_dir, lib))
    ctypes.cdll.LoadLibrary(os.path.join(lib_dir, lib))

from . import bpy

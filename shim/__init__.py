import ctypes
import os

lib_dir = os.path.dirname(os.path.realpath(__file__))

LIBRARIES = [
    'libHalf.so',
    'libIex.so',
    'libIexMath-2_4.so.24',
    'libImath.so',
    'libIlmThread.so',
    'libIlmImf.so',
    'libboost_chrono.so.1.70.0',
    'libboost_date_time.so.1.70.0',
    'libboost_system.so.1.70.0',
    'libboost_filesystem.so.1.70.0',
    'libboost_regex.so.1.70.0',
    'libboost_thread.so.1.70.0',
    'libboost_wave.so.1.70.0',
    'libpython3.7m.so.1.0',
    'libGLU.so.1',
    'libfftw3.so.3',
    'libopenjpeg.so.2',
    'libOpenImageIO.so',
    'libGLEW.so.2.2',
    'liboslcomp.so.1.10',
    'liboslexec.so.1.10',
    'liboslquery.so.1.10',
    'libosdCPU.so.3.4.0',
    'libosdGPU.so.3.4.0',
]

for lib in LIBRARIES:
    print(os.path.join(lib_dir, lib))
    ctypes.cdll.LoadLibrary(os.path.join(lib_dir, lib))

from . import bpy

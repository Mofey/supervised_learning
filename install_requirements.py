import os
import sys
import subprocess

REQUIRED_LIBS = ['pandas', 'scikit-learn']
for lib in REQUIRED_LIBS:
    try:
        __import__(lib)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
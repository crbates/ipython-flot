from __future__ import print_function

# setuptools must be imported for "python setup.py develop" to work.
import setuptools

from distutils.core import setup
import string
import sys

import IPython

baseversion = int(string.split(IPython.__version__,'.')[1])
if baseversion < 13:
    print("IPython version >= 0.13 required")
    sys.exit(1)

setup(name="ipython_flot",
      author="Cameron Bates",
      py_modules = ['flotplot'],
      )

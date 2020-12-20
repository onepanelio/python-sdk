from __future__ import absolute_import

from onepanel.nbextensions.magics import IPythonMagics

def load_ipython_extension(ipython):
    ipython.register_magics(IPythonMagics)

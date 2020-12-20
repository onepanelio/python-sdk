from .magics import IPythonMagics

def load_ipython_extension(ipython):
    ipython.register_magics(IPythonMagics)

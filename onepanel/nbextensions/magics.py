import os

from IPython.core.magic import (Magics, magics_class, line_magic)
from IPython.display import IFrame

@magics_class
class IPythonMagics(Magics):

    @line_magic
    def nni_ui(self, line):
        src = '//{uid}--{namespace}.{domain}/nni'.format(
            uid=os.getenv('ONEPANEL_RESOURCE_UID'),
            namespace=os.getenv('ONEPANEL_RESOURCE_NAMESPACE'),
            domain=os.getenv('ONEPANEL_DOMAIN'))
        return IFrame(src=src, width='100%', height='500px')

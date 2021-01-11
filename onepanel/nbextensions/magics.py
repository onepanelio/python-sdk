import os

from IPython.core.magic import (Magics, magics_class, line_magic)
from IPython.display import IFrame

@magics_class
class IPythonMagics(Magics):

    @line_magic
    def nni_ui(self, line):
        domain = os.getenv('ONEPANEL_DOMAIN', 'localhost')

        if domain == 'localhost':
            src = '//{domain}:8080'.format(domain=domain, port=port)
        else:
            src = '//{uid}--{namespace}.{domain}/nni'.format(
                uid=os.getenv('ONEPANEL_RESOURCE_UID'),
                namespace=os.getenv('ONEPANEL_RESOURCE_NAMESPACE'),
                domain=domain)
        return IFrame(src=src, width='100%', height='500px')

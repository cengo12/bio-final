import sys, os
if sys.executable.endswith('pythonw.exe'):
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.path.join(os.getenv('TEMP'), 'stderr-{}'.format(os.path.basename(sys.argv[0]))), "w")
    
import logging
import webview
from contextlib import redirect_stdout
from io import StringIO
from server import server

logger = logging.getLogger(__name__)

if __name__ == '__main__':

    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window('My first pywebview application', server)
        webview.start()
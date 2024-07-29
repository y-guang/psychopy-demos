# this script just wait 5 second and attach the argument to a file

import time
import pathlib
import sys

TOOL_FOLDER = pathlib.Path(__file__).resolve().parent
RECORD_PATH = TOOL_FOLDER / 'record.txt'

if __name__ == '__main__':
    time.sleep(5)
    with open(RECORD_PATH, 'w') as f:
        f.write(' '.join(sys.argv[1:]))
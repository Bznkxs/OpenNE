import time
import os
import sys
import platform
if __name__ == "__main__":
    curdir = os.path.abspath(__file__)[:-os.path.basename(__file__).__len__()]
    os.chdir(curdir)
    pff = "00_logs_to_md.py"
    while True:


        if platform.system() == 'Windows':
            os.system("python "+ pff)
        else:
            os.system("python3 "+ pff)
        time.sleep(10)
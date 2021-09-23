import numpy as np
import sys
from time import sleep
from init_system import SysInit

__author__ = 'lha'
__version__ = '1.0.0a'

if __name__ == '__main__':
    ex = SysInit()
    ex.info_out('console')
    sleep(1)
    print("show must go on!")



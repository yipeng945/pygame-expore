#!/usr/bin/env python

import sys
import pygame as pyg
from data.main import main
import cProfile


if __name__ == "__main__":
    main()
    pyg.quit()
    sys.exit()

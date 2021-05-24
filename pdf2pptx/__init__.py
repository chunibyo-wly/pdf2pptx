import os

PACKAGE_BASE_PATH = os.path.dirname(os.path.abspath(__file__))
__version__ = open(os.path.join(PACKAGE_BASE_PATH, "version")).read().splitlines()[0]

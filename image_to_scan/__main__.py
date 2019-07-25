# -*- coding: utf-8 -*-


"""
The main entry point. Invoke as `photo-to-scan'
"""
import sys

from .core import main as _main


def main():
    try:
        sys.exit(_main())
    except KeyboardInterrupt:
        from . import ExitStatus

        sys.exit(ExitStatus.ERROR_CTRL_C)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


"""
The main entry point. Invoke as `photo-to-scan'
"""
import sys

from .image_to_scan import main as _main


def main():
    try:
        sys.exit(_main())
    except KeyboardInterrupt:
        from . import ExitStatus

        sys.exit(ExitStatus.ERROR_CTRL_C)


if __name__ == "__main__":
    main()

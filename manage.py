#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

BANNER = r"""
                         _     _                         __      __      __  
                        | |   | |                       / /     / /     / /  
   ___   _ __    _   _  | |_  | |__     ___    _ __    / /_    / /_    / /_  
  / __| | '_ \  | | | | | __| | '_ \   / _ \  | '_ \  | '_ \  | '_ \  | '_ \ 
 | (__  | |_) | | |_| | | |_  | | | | | (_) | | | | | | (_) | | (_) | | (_) |
  \___| | .__/   \__, |  \__| |_| |_|  \___/  |_| |_|  \___/   \___/   \___/ 
        | |       __/ |                                                      
        |_|      |___/                                                       
访问我的博客：https://cpython666.github.io/
访问我的博客：https://stardreamfly.github.io/
"""


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LearnSpider.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if "runserver" in sys.argv:
        if not os.environ.get("RUN_MAIN", None):
            print(BANNER)  # Print the banner only if RUN_MAIN is not set
    else:
        print(BANNER)
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

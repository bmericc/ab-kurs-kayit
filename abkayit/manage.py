#!-*- coding:utf-8 -*-
#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "abkayit.settings")
    import sys
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(BASE_DIR, "abkayit"))

    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command as runserver

    runserver.default_port = "8001" 

    execute_from_command_line(sys.argv)

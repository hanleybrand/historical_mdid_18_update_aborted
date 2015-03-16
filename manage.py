#!/usr/bin/env python
import os
import sys

# enable drop in pymysql replacement of python-mysqldb
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

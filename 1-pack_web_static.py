#!/usr/bin/python3
"""generate a .tgz archive from web_static folder"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """generate a .tgz archive from web_static folder"""
    create_time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(create_time)
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None

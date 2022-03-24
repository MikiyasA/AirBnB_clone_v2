#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ method to generates a .tgz
    """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        time = datetime.now()
        formt = "%Y%m%d%H%M%S"
        arch_path = 'versions/web_static_{}.tgz'.format(time.strftime(formt))
        local('tar -cvzf {} web_static'.format(arch_path))
        return arch_path
    except Exception:
        return None

#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy
"""
from datetime import datetime
from fabric.api import *
import shlex
import os


env.hosts = ['34.148.170.206', '3.226.243.40']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploys """

    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        wname = name.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(name)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """ Deploys """
    try:
        archive_path = do_pack()
    except Exception:
        return False
    return do_deploy(archive_path)


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        time = datetime.now()
        frmt = "%Y%m%d%H%M%S"
        arch_path = 'versions/web_static_{}.tgz'.format(time.strftime(frmt))
        local('tar -cvzf {} web_static'.format(arch_path))
        return arch_path
    except Exception:
        return None

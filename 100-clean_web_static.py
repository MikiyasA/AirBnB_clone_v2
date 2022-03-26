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

def do_clean(number=0):
    """ Clean archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1
       
    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))

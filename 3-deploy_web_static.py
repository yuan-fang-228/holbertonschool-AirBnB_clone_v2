#!/usr/bin/python3
"""create and distribute an archive to web servers"""
from datetime import datetime
from fabric.api import *
import os
env.hosts = ['34.207.236.163', '107.20.69.130']


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


def do_deploy(archive_path):
    """distribute an archive to web server, false if path not exist"""
    if not os.path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        onlyfilename = filename.split(".")[0]
        uncompressfd = "/data/web_static/releases/{}/".format(onlyfilename)
        run("mkdir -p {}".format(uncompressfd))
        run("tar -zxvf /tmp/{} -C {}".format(filename, uncompressfd))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}/".format(uncompressfd, uncompressfd))
        run("rm -rf {}web_static".format(uncompressfd))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(uncompressfd))
        return True
    except Exception:
        return False


def deploy():
    """function that create and distribute an archive to web servers"""
    filepath = do_pack()
    if filepath is None:
        return False
    return do_deploy(filepath)

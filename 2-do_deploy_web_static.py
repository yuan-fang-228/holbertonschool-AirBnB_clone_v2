#!/usr/bin/python3
"""distribute an archive to web server"""
import os
from fabric.api import run, put, env
env.hosts = ['34.207.236.163', '107.20.69.130']


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

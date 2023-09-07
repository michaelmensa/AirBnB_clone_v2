#!/usr/bin/python3

'''
Fabric script that generates a .tgz archive from the contents of
the web_static folder of AirBnB_clone repo, using function do_pack.
'''


from fabric.api import *
from datetime import datetime
import os

env.hosts = ['100.25.38.204', '52.23.212.54']
env.user = 'ubuntu'


def do_pack():
    '''
    Compresses the web_static folder into a .tgz archive.
    Returns the path to the archive on success, None on failure
    '''
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f'web_static_{timestamp}.tgz'
        archive_path = local(f'tar -czvf versions/{archive_name} web_static/')
        return archive_path
    except Exception as e:
        print("An exception occurred: {}".format(e))
        return None


def do_deploy(archive_path):
    '''
    Deploys archive to web servers
    Parameters: archive_path(str): path to deploy
    Return: False if archive_path doesn't exists or errors otherwise True
    '''
    if not os.path.exists(archive_path):
        return False
    try:
        tgz_file = archive_path.split('/')[-1]
        fname = tgz_file.split('.')[0]

        '''upload archive to /tmp/directiory on web server'''
        put(archive_path, '/tmp/')

        releases_path = f'/data/web_static/releases/{fname}/'
        run(f'mkdir -p {releases_path}')

        '''extracts archive and delete .tgz'''
        run(f'sudo tar -xzf /tmp/{tgz_file} -C {releases_path}')
        run(f'sudo rm /tmp/{tgz_file}')

        '''delete symbolic link /data/web_static/current if exists'''
        run('sudo rm -rf /data/web_static/current')

        '''create a new symbolic link /data/web_static/current'''
        run(f'sudo ln -s {releases_path} /data/web_static/current')
        print('New version deployed!')
    except Exception as e:
        print(f'An exception occured: {e}')
        return False


def deploy():
    '''creates and deploys an archive to web servers
    '''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

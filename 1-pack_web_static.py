#!/usr/bin/python3

'''
Fabric script that generates a .tgz archive from the contents of
the web_static folder of AirBnB_clone repo, using function do_pack.
'''


from fabric.api import local
from datetime import datetime
import os


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

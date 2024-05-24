#!/usr/bin/python3
"""This file will pack the contents of the web_static directory"""

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    if not os.path.exists("versions"):
        os.mkdir("versions")
    archive_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{archive_time}"

    try:
        local(f"tar -czvf versions/{archive_name}.tar.gz web_static")
        return f"versions/{archive_name}"
    except:
        print("error")
        return None

EasyWebDAV: A WebDAV Client in Python
=====================================

Features
--------

* Basic authentication
* Creating directories, removing directories and files
* Uploading and downloading files
* Directory listing

Installation
------------

Install using distribute:

    easy_install easywebdav

Quick Start
-----------

    import easywebdav
    # Start off by creating a client object. Username and
    # password may be omitted if no authentication is needed.
    webdav = easywebdav.connect('webdav.your-domain.com', username='myuser', password='mypass')
    # Do some stuff:
    webdav.mkdir('some_dir')
    webdav.rmdir('another_dir')
    webdav.download('remote/path/to/file', 'local/target/file')
    webdav.upload('local/path/to/file', 'remote/target/file')

Client object API
-----------------

The API is pretty much self-explanatory:

    cd(path)
    mkdir(path, safe=False)
    mkdirs(path)
    rmdir(path, safe=False)
    delete(file_path)
    upload(local_path, remote_path)
    download(remote_path, local_path)

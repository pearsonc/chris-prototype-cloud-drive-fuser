This project is to create a simple fuse filesystem for commandline only systems allowing you to connect with multiple cloud storage providers.

I have started this project to advance on astrada/google-drive-ocamlfuse project by adding amazon drive, dropbox, onedrive and google drive.

Also I am developing in Python rather than Ocaml.

It is still in the dev stage and I am periodically working on it.

Currently this only mounts a folder on a file system as a fuse mount and has a long way to go before it is useable.
I am also making use of cement to provide a decent CLI interface.

The google drive extention has the FuseLib function calls but currently they just map to unix os commands, I need to remove these and replace with google drive API method calls and thats just the start of the many things that needs to happen.

I have made this public so anyone who is intrested can clone and use in anyway they want or just so you can see how I am going about this development.

Cloud Drive Fuser
==============================================================================

Installation
------------

```
$ pip install -r requirements.txt

$ python setup.py install
```

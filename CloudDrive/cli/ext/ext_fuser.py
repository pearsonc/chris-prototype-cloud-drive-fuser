from cement.utils.misc import minimal_logger
from fuse import FUSE
import os
import threading
from CloudDrive.cli.ext.google_drive_operations import PearsonnetGoogleDrive

LOG = minimal_logger(__name__)
# CODE HANDLERS, HOOKS, ETC HERE

# This is currently a pass through service looping fuse calls through the os module for testing purposes.
# Once testing is complete os should be replaced with plugins to cloud providers.
# This service should be designed to connect to multiple cloud providers at once.
# Also this should possibly include a cloud sync method in the future.


class PearsonnetFuse:
    def __init__(self, mount_point, root):
        self.root = root
        self.mountPoint = mount_point
        self.t = ''

    def mount(self):
        print(os.path.isdir(self.root))
        print(os.path.isdir(self.mountPoint))
        if len(os.listdir(self.mountPoint)) == 0:
            print(self.mountPoint+" Directory is empty")
        self.t = threading.Thread(name='child procs', target=self.mounter())
        self.t.start()

    def mounter(self):
        FUSE(
            PearsonnetGoogleDrive(self.root),
            self.mountPoint,
            nothreads=True,
            foreground=False,
            **{'allow_other': True}
        )


def load(app):
    pass

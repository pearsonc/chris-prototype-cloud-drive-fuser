"""Cloud Drive Fuser base controller."""

from cement.ext.ext_argparse import ArgparseController, expose
from CloudDrive.cli.ext.ext_fuser import PearsonnetFuse


class PearsonnetBaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = "Uses Fuse to bind cloud drive services to unix based filesystems. \n" \
                      "use umount /path/to/mount to disconnect and stop the daemon/service"

    @expose(hide=True)
    def default(self):
        # try catch required here to handle failure
        obj = PearsonnetFuse('/Users/chrispearson/Documents/20051/Pearsonnet/Projects/Python/cdf/test',
                             '/Users/chrispearson/test')
        obj.mount()

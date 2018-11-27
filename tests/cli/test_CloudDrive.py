"""CLI tests for CloudDrive."""

from CloudDrive.utils import test


class CliTestCase(test.PearsonnetTestCase):
    def test_CloudDrive_cli(self):
        argv = ['--foo=bar']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.foo, 'bar')

"""Fuser Framework Extension Tests."""

from cement.utils import test

class PearsonnetExtTestCase(test.CementTestCase):
    def setUp(self):
        super(PearsonnetExtTestCase, self).setUp()
        self.app = self.make_app('tests', extensions=['CloudDrive.cli.ext.fuser'])

    def test_fuser(self):
        self.app.setup()
        self.app.run()

        ### DO SOMETHING TO TEST fuser

        self.app.close()

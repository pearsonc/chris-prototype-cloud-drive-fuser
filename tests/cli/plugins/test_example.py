"""Tests for Example Plugin."""

from CloudDrive.utils import test

class ExamplePluginTestCase(test.PearsonnetTestCase):
    def test_load_example_plugin(self):
        self.app.setup()
        self.app.plugin.load_plugin('example')

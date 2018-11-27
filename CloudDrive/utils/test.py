"""Testing utilities for Cloud Drive Fuser."""

from CloudDrive.cli.main import PearsonnetTestApp
from cement.utils.test import *

class PearsonnetTestCase(CementTestCase):
    app_class = PearsonnetTestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(PearsonnetTestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(PearsonnetTestCase, self).tearDown()


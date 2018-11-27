"""Cloud Drive Fuser bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as PearsonnetBaseController.

from CloudDrive.cli.controllers.base import PearsonnetBaseController

def load(app):
    app.handler.register(PearsonnetBaseController)

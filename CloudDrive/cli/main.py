"""Cloud Drive Fuser main application entry point."""

from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults
from cement.core.exc import FrameworkError, CaughtSignal
from CloudDrive.core import exc


defaults = init_defaults('CloudDrive', 'daemon', 'log.logging')
defaults['log.logging']['file'] = 'my.log'
defaults['CloudDrive']['plugin_config_dir'] = '/etc/CloudDrive/plugins.d'
defaults['CloudDrive']['plugin_dir'] = '/var/lib/CloudDrive/plugins'
defaults['CloudDrive']['template_dir'] = '/var/lib/CloudDrive/templates'


class PearsonnetApp(CementApp):
    class Meta:
        label = 'CloudDrive'
        extensions = ['CloudDrive.cli.ext.ext_fuser']
        config_defaults = defaults

        # All built-in application bootstrapping (always run)
        bootstrap = 'CloudDrive.cli.bootstrap'

        # Internal plugins (ship with application code)
        plugin_bootstrap = 'CloudDrive.cli.plugins'

        # Internal templates (ship with application code)
        template_module = 'CloudDrive.cli.templates'

        # call sys.exit() when app.close() is called
        exit_on_close = True


class PearsonnetTestApp(PearsonnetApp):
    """A test app that is better suited for testing."""
    class Meta:
        # default argv to empty (don't use sys.argv)
        argv = []

        # don't look for config files (could break tests)
        config_files = []

        # don't call sys.exit() when app.close() is called in tests
        exit_on_close = False


# Define the applicaiton object outside of main, as some libraries might wish
# to import it as a global (rather than passing it into another class/func)
app = PearsonnetApp()


def main():

    with app:
        try:
            app.log.info('App Starting')
            app.run()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            app.close()
            app.log.info('CaughtSignal > %s' % e)
            app.exit_code = 0
        
        except exc.PearsonnetError as e:
            # Catch our application errors and exit 1 (error)
            app.log.info('PearsonnetError > %s' % e)
            app.exit_code = 1
            
        except FrameworkError as e:
            # Catch framework errors and exit 1 (error)
            app.log.info('FrameworkError > %s' % e)
            app.exit_code = 1


if __name__ == '__main__':
    main()

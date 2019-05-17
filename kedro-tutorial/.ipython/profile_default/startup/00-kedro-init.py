import logging.config
import os

from IPython.core.magic import register_line_magic


@register_line_magic
def reload_kedro(line=None):
    """"Line magic which reloads all Kedro default variables."""
    global proj_dir
    global proj_name
    global conf
    global io
    global startup_error
    try:
        import kedro.config.default_logger
        from kedro_tutorial.run import create_catalog, get_config

        proj_name = "Kedro Tutorial"
        logging.info("** Kedro project {}".format(proj_name))

        os.chdir(proj_dir)  # Move to project root

        # Load Kedro context (conf, io, parameters)
        conf = get_config(proj_dir)
        io = create_catalog(conf)

        logging.info("Defined global variables proj_dir, proj_name, conf and io")
    except ImportError as err:
        startup_error = err
        if "create_catalog" in str(err):
            message = (
                "The function `create_catalog` is missing from "
                "kedro-tutorial/src/"
                "kedro_tutorial/run.py."
                "\nEither restore this function, or update "
                "kedro-tutorial/"
                ".ipython/profile_default/startup/00-kedro-init.py."
            )
        elif "get_config" in str(err):
            message = (
                "The function `get_config` is missing from "
                "kedro-tutorial/src/"
                "kedro_tutorial/run.py."
                "\nEither restore this function, or update "
                "kedro-tutorial/"
                ".ipython/profile_default/startup/00-kedro-init.py."
            )
        else:
            message = (
                "Kedro appears not to be installed in your " "current environment."
            )
        logging.error(message)
        raise err
    except Exception as err:
        startup_error = err
        logging.error("Kedro's ipython session startup script failed:\n%s", str(err))
        raise err


# Find the project root (./../../../)
startup_error = None
proj_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir)
)
reload_kedro()

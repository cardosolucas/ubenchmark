import os
import logging

DEFAULT_LOG_LEVEL = logging.DEBUG
DEFAULT_LOG_DIR = os.environ['UBENCH_LOG']


class Logger(logging.getLoggerClass()):
    """Custom logger class.

    Use this class to customize the logger behavior or to intercept the
    messages.
    """
    # def error(self, msg, *args, **kwargs):
    #     # Add here code to intercept the project error messages
    #     super(Logger, self).error(msg, *args, **kwargs)

    # def critical(self, msg, *args, **kwargs):
    #     # Add here code to intercept the project critical messages
    #     super(Logger, self).critical(msg, *args, **kwargs)


logging.setLoggerClass(Logger)


def get_logger(name, namespace='house-prices-benchmark',
               log_level=DEFAULT_LOG_LEVEL, log_dir=DEFAULT_LOG_DIR):
    """Build a logger that outputs to a file and to the console,"""

    log_level = (os.getenv('{}_LOG_LEVEL'.format(namespace.upper())) or
                 os.getenv('LOG_LEVEL', log_level))
    log_dir = (os.getenv('{}_LOG_DIR'.format(namespace.upper())) or
               os.getenv('LOG_DIR', log_dir))

    logger = logging.getLogger('{}.{}'.format(namespace, name))
    logger.setLevel(log_level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a console stream handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    try:
        log_path = os.path.abspath(log_dir)
        log_filename = '{name}.{pid}.log'.format(
            name=namespace, pid=os.getpid())

        file_path = str(os.path.join(log_path, log_filename))

        if not os.path.exists(log_path):
            os.makedirs(log_path)

        file_handler = logging.FileHandler(file_path)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except OSError as e:
        logger.error('Could not create log file {file}: {error}'.format(
            file=file_path, error=e.strerror))

    return logger
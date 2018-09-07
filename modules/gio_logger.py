import logging
import logging.handlers
from pathlib import Path
import os

module_name = __name__
log = logging.getLogger(module_name)

#Path definer
def _config_path(path, filename=''):
    this_dir = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(this_dir, '..', path, filename))

#Logger
def get_top_level_logger(name, log_filename='logs/tree_exercise.log', log_target='terminal'):
    LOG_LEVELS = {'debug'   : logging.DEBUG,
                  'info'    : logging.INFO,
                  'warning' : logging.WARNING,
                  'error'   : logging.ERROR,
                  'critical': logging.CRITICAL}

    log_filename = _config_path(log_filename)

    def get_log_level():
        requested_loglevel = os.environ.get('GIO_LOG_LEVEL', 'info').lower()
        loglevel = LOG_LEVELS[requested_loglevel if requested_loglevel in LOG_LEVELS else 'info']
        return loglevel

    valid_targets = ['file','terminal']
    if log_target not in valid_targets:
        raise ValueError('The log_target parameter must be one of {}'.format(valid_targets))
    elif log_target == 'file' and not log_filename:
        raise ValueError('You must specify the log_filename parameter.')

    logger = logging.getLogger(name)
    if log_target == 'terminal':
        handler = logging.StreamHandler()
    else:
        handler = logging.handlers.RotatingFileHandler(log_filename,
                maxBytes=1024 * 1024 * 15,
                backupCount=15)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(get_log_level())
    return logger

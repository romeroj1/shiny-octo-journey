import os
import logging
import logging.handlers

def get_logger(name='FabricLogger', path_for_log='c:\temp', file_name='vetbackups.log'):
    # type: (object, object, object) -> object
    #output path and file name
    log_file = os.path.join(path_for_log, file_name)

    # Create logger
    my_logger = logging.getLogger(name)
    my_logger.setLevel(logging.INFO)

    my_logger.handlers = []

    # Create console handler and set level to debug
    file_handler = logging.handlers.RotatingFileHandler(filename=log_file, mode='a', maxBytes=26214400, backupCount=5, encoding='utf-8', delay=False)
    file_handler.setLevel(logging.INFO)

    # Create Formatter
    formatter = logging.Formatter(fmt='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    my_logger.addHandler(file_handler)

    my_logger.propagate = False

    return my_logger
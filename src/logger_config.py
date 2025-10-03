
import logging
import logging.handlers
import multiprocessing
import sys


def setup_async_logger():
    log_queue = multiprocessing.Queue()

    queue_handler = logging.handlers.QueueHandler(log_queue)
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(queue_handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(fmt="%(levelname)s:     %(asctime)s - %(name)s - %(message)s",
                                  datefmt="%Y-%m-%d %H:%M:%S")
    stream_handler.setFormatter(formatter)

    listener = logging.handlers.QueueListener(log_queue, stream_handler)
    listener.start()
    
    return listener

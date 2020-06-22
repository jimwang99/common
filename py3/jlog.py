import logging

class CustomFileFormatter(logging.Formatter):
    # {{{

    def __init__(self):
        super().__init__(fmt="%(levelno)d: %(msg)s", datefmt=None, style='%')  

        self.fmt_dbg     = "%(name)s:DBG %(msg)s"
        self.fmt_info    = "%(name)s:INF %(msg)s"
        self.fmt_warn    = "%(name)s:WARNING %(msg)s\n    @ file=%(pathname)s line=%(lineno)d"
        self.fmt_err     = "%(name)s:ERROR %(msg)s\n    @ file=%(pathname)s line=%(lineno)d"

    def format(self, record):
        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._style._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == logging.DEBUG:
            self._style._fmt = self.fmt_dbg

        elif record.levelno == logging.INFO:
            self._style._fmt = self.fmt_info

        elif record.levelno == logging.WARNING:
            self._style._fmt = self.fmt_warn

        elif record.levelno == logging.ERROR:
            self._style._fmt = self.fmt_err

        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)

        # Restore the original format configured by the user
        self._style._fmt = format_orig

        return result
    # }}}

class CustomConsoleFormatter(CustomFileFormatter):
    # {{{

    def __init__(self):
        ascii_red = "\033[1;31m"
        ascii_green = "\033[1;32m"
        ascii_yellow = "\033[1;33m"
        ascii_reset = "\033[0m"

        super().__init__()
        self.fmt_info   = ascii_green + self.fmt_info + ascii_reset;
        self.fmt_warn   = ascii_yellow + self.fmt_warn + ascii_reset;
        self.fmt_err    = ascii_red + self.fmt_err + ascii_reset;

    # }}}

def get_logger(name, fname=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if (fname is not None):
        h_file = logging.FileHandler(fname, 'w')
        h_file.setFormatter(CustomFileFormatter())
        h_file.setLevel(logging.DEBUG)
        logger.addHandler(h_file)

    h_console = logging.StreamHandler()
    h_console.setFormatter(CustomConsoleFormatter())
    h_console.setLevel(logging.DEBUG)
    logger.addHandler(h_console)

    return logger

if __name__ == '__main__':
    logger = get_logger('test0-logger', 'test0.log')
    logger.debug('debug-debug-debug')
    logger.info('info-info-info')
    logger.warning('warning-warning-warning')
    logger.error('error-error-error')

    logger1 = get_logger('test1-logger', 'test1.log')
    logger1.debug('debug-debug-debug')
    logger1.info('info-info-info')
    logger1.warning('warning-warning-warning')
    logger1.error('error-error-error')


# class Log():
# 
#     def __init__(self, name='ROOT', fname=None, logger=None):
#         if (logger is None):
#             self.logger = Log.init_logger(fname)
#         else:
#             self.logger = logger
# 
#     @staticmethod
#     def init_logger(fname):
#         # {{{
# 
#         logger = logging.getLogger()
# 
#         if (fname is not None):
#             h_file = logging.FileHandler(fname, 'w')
#             h_file.setFormatter(CustomFormatter())
#             h_file.setLevel(logging.DEBUG)
#             logger.addHandler(h_file)
# 
#         h_console = logging.StreamHandler()
#         h_console.setFormatter(CustomColoredFormatter())
#         h_console.setLevel(logging.DEBUG)
#         logger.addHandler(h_console)
# 
#         logger.setLevel(logging.DEBUG)
# 
#         return logger
#         # }}}
# 
#     def has_error(self):
#         return (self.logger.error.count > 0)
# 
#     def debug(self, tag, s):
#         self.logger.debug(f':{tag:8} {s}')
# 
#     def info(self, tag, s):
#         self.logger.info(f':{tag:8} {s}')
# 
#     def warning(self, tag, s):
#         self.logger.warning(f':{tag} {s}')
# 
#     def error(self, tag, s):
#         self.logger.error(f':{tag} {s}')
# 
# if __name__ == '__main__':
#     log = Log(name='TEST', fname='test_Log.log')
#     # print('eff-level=', log.logger.getEffectiveLevel(), 'debug-level=', logging.DEBUG)
#     log.logger.debug('debug-debug-debug')
#     log.logger.info('info-info-info')
#     log.logger.warning('warning-warning-warning')
#     log.logger.error('error-error-error')
# 
#     log.debug('tag-d', 'debug-debug-debug')
#     log.debug('tag-dd', 'debug-debug-debug')
#     log.debug('tag-ddd', 'debug-debug-debug')
#     log.debug('tag-dddd', 'debug-debug-debug')
#     log.info('tag-i', 'info-info-info')
#     log.info('tag-ii', 'info-info-info')
#     log.info('tag-iii', 'info-info-info')
#     log.info('tag-iiii', 'info-info-info')
#     log.warning('tag-w', 'warning-warning-warning')
#     log.error('tag-e', 'error-error-error')

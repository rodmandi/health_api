import logging
import traceback
import sys

FORMAT = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
ROOT_FORMAT = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%m/%d/%Y %H:%M:%S %Z'
LOGGER_LEVEL = logging.INFO


class DefaultLogger:
    """
    Setup of a logger object
    """
    def __init__(self):
        pass

    @classmethod
    def get_logger(cls, name='default'):
        """
        Creates a Logger object with a defined name. Adds a handler and the output is not propagated
        to the parent logger
        :param name: name of the logger object
        :type name: str
        :return: logging.Logger
        """
        module_logger = LoggerCustom(name)
        module_formatter = CustomFormatter(fmt=FORMAT, datefmt=DATE_FORMAT)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(LOGGER_LEVEL)
        console_handler.setFormatter(module_formatter)
        module_logger.propagate = False
        module_logger.addHandler(console_handler)
        return module_logger

    @classmethod
    def set_root_logger_basic_config(cls):
        """
        Sets the root logger basic config. Sets a StreamHandler with DEBUG level and uses the ROOT_FORMAT and
        DATE_FORMAT global variables for log format
        :return:
        """
        console_handler = logging.StreamHandler()
        console_handler.setLevel(LOGGER_LEVEL)
        logging.basicConfig(format=ROOT_FORMAT,
                            datefmt=DATE_FORMAT,
                            handlers=[console_handler],
                            level=LOGGER_LEVEL)


def get_custom_error_message():
    return traceback.format_exc().replace("\n", "\\n")


class LoggerCustom(logging.Logger):
    """
    Logger class that overrides the logging.Logger
    """

    def info(self, msg, id=None, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'. This function overrides logging.Logger
        :param msg: msg to show in the logs
        :param id: the input given instead of the extra parameter
        :param args:
        :param kwargs:
        :return: a log with the format given
        """
        if id is None:
            return super(LoggerCustom, self).info(msg, *args, **kwargs)
        else:
            return super(LoggerCustom, self).info(f"{id} - {msg}", *args, **kwargs)

    def debug(self, msg, id=None, *args, **kwargs):
        """
        Log 'msg % args' with severity 'DEBUG'. This function overrides logging.Logger
        :param msg: msg to show in the logs
        :param id: the input given instead of the extra parameter
        :param args:
        :param kwargs:
        :return: a log with the format given
        """
        if id is None:
            return super(LoggerCustom, self).debug(msg, *args, **kwargs)
        else:
            return super(LoggerCustom, self).debug(f"{id} - {msg}", *args, **kwargs)

    def error(self, msg, id=None, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'. This function overrides logging.Logger
        :param msg: msg to show in the logs
        :param id: the input given instead of the extra parameter
        :param args:
        :param kwargs:
        :return: a log with the format given
        """
        if id is None:
            return super(LoggerCustom, self).error(msg, *args, **kwargs)
        else:
            return super(LoggerCustom, self).error(f"{id} - {msg}", *args, **kwargs)

    def warning(self, msg, id=None, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'. This function overrides logging.Logger
        :param msg: msg to show in the logs
        :param id: the input given instead of the extra parameter
        :param args:
        :param kwargs:
        :return: a log with the format given
        """
        if id is None:
            return super(LoggerCustom, self).warning(msg, *args, **kwargs)
        else:
            return super(LoggerCustom, self).warning(f"{id} - {msg}", *args, **kwargs)

    def exception(self, msg, id=None, *args, **kwargs):
        """
        Log 'msg % args' with severity 'EXCEPTION'. This function overrides logging.Logger
        :param msg: msg to show in the logs
        :param id: the input given instead of the extra parameter
        :param args:
        :param kwargs:
        :return: a log with the format given
        """
        if id is None:
            return super(LoggerCustom, self).exception(msg, *args, **kwargs)
        else:
            return super(LoggerCustom, self).exception(f"{id} - {msg}", *args, **kwargs)


class CustomFormatter(logging.Formatter):
    def format(self, record):
        """
        Format the specified record as text.

        The record's attribute dictionary is used as the operand to a
        string formatting operation which yields the returned string.
        Before formatting the dictionary, a couple of preparatory steps
        are carried out. The message attribute of the record is computed
        using LogRecord.getMessage(). If the formatting string uses the
        time (as determined by a call to usesTime(), formatTime() is
        called to format the event time. If there is exception information,
        it is formatted using formatException() and appended to the message.
        """
        record.message = record.getMessage()
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        try:
            s = self._fmt % record.__dict__
        except UnicodeDecodeError as e:
            # Issue 25664. The logger name may be Unicode. Try again ...
            try:
                record.name = record.name.decode('utf-8')
                s = self._fmt % record.__dict__
            except UnicodeDecodeError:
                raise e
        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            try:
                s = s + ' - ' + record.exc_text
                s = s.replace('\n', '\\n')
            except UnicodeError:
                # Sometimes filenames have non-ASCII chars, which can lead
                # to errors when s is Unicode and record.exc_text is str
                # See issue 8924.
                # We also use replace for when there are multiple
                # encodings, e.g. UTF-8 for the filesystem and latin-1
                # for a script. See issue 13232.
                s = s + record.exc_text.decode(sys.getfilesystemencoding(),
                                               'replace')
        return s

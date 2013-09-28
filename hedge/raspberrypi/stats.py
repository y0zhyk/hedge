import json
import os
import datetime


def cpu_usage():
    """Retrieves information about cpu usage"""
    percent = 0
    try:
        import psutil

        percent = psutil.cpu_percent()
    except ImportError:
        pass
    return percent, "{}%".format(percent)


def memory_usage():
    """Retrieves information about memory usage"""
    percent = 0
    value = ""
    try:
        import psutil

        usage = psutil.virtual_memory()
        percent = usage.percent
        value = "({}/{})".format(usage.used, usage.total)
    except ImportError:
        pass
    return percent, value


def swap_usage():
    """Retrieves information about swap memory usage"""
    percent = 0
    value = ""
    try:
        import psutil

        usage = psutil.swap_memory()
        percent = usage.percent
        value = "({}/{})".format(usage.used, usage.total)
    except ImportError:
        pass
    return percent, value


def disk_usage():
    """Retrieves information about swap disk usage"""
    percent = 0
    value = ""
    try:
        import psutil

        usage = psutil.disk_usage('/')
        percent = usage.percent
        value = "({}/{})".format(usage.used, usage.total)
    except ImportError:
        pass
    return percent, value


def cpu_temperature():
    """Retrieves information about CPU temperature"""
    value = 0
    try:
        res = os.popen('vcgencmd measure_temp').readline()
        value = float(res.replace("temp=", "").replace("'C\n", ""))
    except ValueError:
        pass
    return value, "{}'C".format(value)


class StatItem(object):
    """Represent progressbar item"""

    def __init__(self, name, description, percent, value):
        self.__name = name
        self.__description = description
        self.__percent = percent
        self.__value = value

    @property
    def description(self):
        """Retrieves display name"""
        return self.__description

    @property
    def name(self):
        """Retrieves internal name"""
        return self.__name

    @property
    def value(self):
        """Retrieves string representation of value"""
        return self.__value

    @property
    def percent(self):
        """Retrieves representation of value in percents"""
        return self.__percent

    def to_dict(self):
        """Returns stat re"""
        return {
            "id": self.name,
            "description": self.description,
            "percent": self.percent,
            "value": self.value
        }


class Stats(object):
    """Represent stat section"""

    def __init__(self):
        self.__time_of_last_update = None
        self.__stats = []

    @staticmethod
    def __now():
        return datetime.datetime.now()

    def __update(self):
        self.__time_of_last_update = self.__now()
        del self.__stats[:]
        self.__stats.extend(
            [
                StatItem('cpu', 'CPU usage', *cpu_usage()),
                StatItem('mem', 'Memory usage', *memory_usage()),
                StatItem('swap', 'Swap usage', *swap_usage()),
                StatItem('disk', 'Disk usage', *disk_usage()),
                StatItem('temp', 'CPU temperature', *cpu_temperature())
            ]
        )

    def to_json(self):
        """Returns JSON representation of stats"""
        self.__update()
        data = dict()
        data["time"] = self.__time_of_last_update.strftime("%Y-%m-%d %H:%M:%S")
        data["stats"] = [stat.to_dict() for stat in self.__stats]
        return json.dumps(data)

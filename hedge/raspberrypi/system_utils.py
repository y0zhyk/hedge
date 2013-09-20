import psutil
import os

def cpu_usage():
    """Retrieves information about cpu usage"""
    return psutil.cpu_percent()


def memory_usage():
    """Retrieves information about memory usage"""
    return psutil.virtual_memory().percent


def swap_usage():
    """Retrieves information about swap memory usage"""
    return psutil.swap_memory().percent


def disk_usage():
    """Retrieves information about swap disk usage"""
    return psutil.disk_usage('/').percent


def cpu_temperature():
    """Retrieves information about CPU temperature"""
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")

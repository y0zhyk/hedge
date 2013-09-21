import os

def cpu_usage():
    """Retrieves information about cpu usage"""
    try:
        import psutil
        return psutil.cpu_percent()
    except ImportError:
        return 0


def memory_usage():
    """Retrieves information about memory usage"""
    try:
        import psutil
        return psutil.virtual_memory().percent
    except ImportError:
        return 0


def swap_usage():
    """Retrieves information about swap memory usage"""
    try:
        import psutil
        return psutil.swap_memory().percent
    except ImportError:
        return 0


def disk_usage():
    """Retrieves information about swap disk usage"""
    try:
        import psutil
        return psutil.disk_usage('/').percent
    except ImportError:
        return 0

def cpu_temperature():
    """Retrieves information about CPU temperature"""
    res = os.popen('vcgencmd measure_temp').readline()
    try:
        return float(res.replace("temp=", "").replace("'C\n", ""))
    except ValueError:
        return 0
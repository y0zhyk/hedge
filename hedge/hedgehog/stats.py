class StatItem(object):
    """Represent progressbar item"""
    def __init__(self, name, display_name):
        self.__name = name
        self.__display_name = display_name

    @property
    def display_name(self):
        """Retrieves display name"""
        return self.__display_name

    @property
    def name(self):
        """Retrieves internal name"""
        return self.__name


class Stats(list):
    """Represent stat section"""
    def __init__(self, items):
        super(Stats, self).__init__()
        self.extend(items)

stats = Stats(
    [
        StatItem(name='cpu',  display_name='CPU usage'),
        StatItem(name='mem',  display_name='Memory usage'),
        StatItem(name='swap', display_name='Swap usage'),
        StatItem(name='disk', display_name='Disk usage')
    ]
)


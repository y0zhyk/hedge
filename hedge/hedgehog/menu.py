from .views import HomeView, AboutView, DLinkView, TorrentView


class MenuItem(object):
    """Represent menu item"""
    def __init__(self, name, display_name, view):
        self.__name = name
        self.__display_name = display_name
        self.__view = view

    @property
    def display_name(self):
        """Retrieves display menu name"""
        return self.__display_name

    @property
    def name(self):
        """Retrieves menu internal name"""
        return self.__name

    @property
    def view(self):
        """Retrieves the view of called menu item"""
        return self.__view


class Menu(list):
    """Represent menu section"""

    def __init__(self, items):
        super(Menu, self).__init__()
        self.extend(items)

menu = Menu(
    [
        MenuItem(name='home',    display_name='Home',    view=HomeView),
        MenuItem(name='d_link',  display_name='D-Link',  view=DLinkView),
        MenuItem(name='torrent', display_name="Torrent", view=TorrentView),
        MenuItem(name='about',   display_name="About",   view=AboutView),
    ]
)


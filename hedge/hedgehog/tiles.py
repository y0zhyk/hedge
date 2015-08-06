
class Tile:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class IconTile(Tile):

    def __init__(self, name, icon):
        super().__init__(1, 1)
        self.__name = name
        self.__icon = icon

    @property
    def name(self):
        return self.__name

    @property
    def icon(self):
        return "images/{}".format(self.__icon)


class Tiles(list):

    def __init__(self, tiles):
        super().__init__()
        self.extend(tiles)


tiles = Tiles(
    [
        IconTile(name="www.raspbian.org", icon="debian_logo.png"),
    ]
)
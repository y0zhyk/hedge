class LogoItem:
    def __init__(self, image, url):
        self.__image = image
        self.__url = url

    @property
    def image(self):
        return "images/{}".format(self.__image)

    @property
    def url(self):
        return "http://{}".format(self.__url)


class Logos(list):
    """Represents site footer"""

    def __init__(self, logos):
        super(Logos, self).__init__()
        self.extend(logos)


logos = Logos(
    [
        LogoItem(image="debian_logo.png", url="www.raspbian.org"),
        LogoItem(image="raspberrypi_logo.png", url="www.raspberrypi.org"),
        LogoItem(image="python_logo.png", url="www.python.org")
    ]
)

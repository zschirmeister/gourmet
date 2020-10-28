from pathlib import Path

from gi.repository.GdkPixbuf import Pixbuf
from PIL import Image, ImageChops

from gourmet.image_utils import (
    bytes_to_image, bytes_to_pixbuf, image_to_bytes, image_to_pixbuf,
    make_thumbnail, pixbuf_to_image, ThumbnailSize)

IMAGE = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xdb\x00C\x01\t\t\t\x0c\x0b\x0c\x18\r\r\x182!\x1c!22222222222222222222222222222222222222222222222222\xff\xc0\x00\x11\x08\x00(\x009\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02w\x00\x01\x02\x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\xf0\x15br\xd1\n\x16$4\xe1%\xf1\x17\x18\x19\x1a&\'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xe4<?\xe1\x9dWR\x10]\xdd\x06\xb6\xf2\xc6\x04\x97\x1f;2\xe0\x00\x02\xf5\x1d\x0er{\x8e:\xd7\xa0Y\xf82\xcd\xa2W\x92\x19J\x91\x87\x9f\x90\xa0\x81\xf9v\xe9^\x8di\xe1\xad7J\xb63\xcc\r\xc3\xc62L\xbd3\x8e\xcb\xd3\xf3\xcf\xd6\xb1\xf5\x9db;\xd0\x89<f8\x94>>V\xdaA\x18\xe4\xe3\xf2\xe9\xf5\xcdy\xf8\xacdhB\xcd\xea\xf6=\x8a*\x83v\xa3\x0en\xed\xff\x00\x91\xe6\x1a\xa6\xa3aa\xa8\x1b8ti.\x95c\x04\xb1l3\x12\xa1\xc7\xcb\xe9\xb7\'<\xe7\xda\xabL\xda<\xed<)a\x0b\x10\xf1\x88D\x91\xc9\x19\x19nA\xf9\xc6\xe6\xc9\xfb\xa3\x18\xe7\x92\x06k\xaf\xf1\x0e\x97\x05\xecwK\x1c&\x061$\x89r\x8aN\x19K\xa0\x19\xff\x00gh\'\x9e\x84\xf1\xc0\xae\x1fX\xf0\xce\xa5\xe1\xeb\x1b\xab\xaf\xb4\x19\xad\xb2\xe3.\xe4\x1d\x81\xd9Q\xb8a\xbb\x8d\xa7\x1d>`0y\xc7\x1d<L\xe6\xb5\x95\x9f\xe6wJ\x9d\n\x91\xe5\x94\x7fO\xc5\x17\xd6O\x0c0kI\xb4\xb6[\xb8HCl\xa5\x8b\x90T6NH\xe7\xaf\x04\xe4c\x9fZ\xdc\xd3\xac4k\xdbG\x9e\xc2\x15\x9a\x10\x15\\\xa6N\xce2\x01\xf4\xeb^{\xa6\xde\xdb\xdb\xde\xa6\xa1k$f\xe68\x82\xc8\x81\x06\xd9s\xcfRA\xdd\x91\x9e=\x97\xa0\xe7\xa7\xb0\xf8\x9b{g&,\x1c[B8T\x08\x19H\x04\xe7#\xd4\x929\xeb\xc0\x02\xba\x15z\x90\x95\x9d\xdc\x7f\x14y\xdc\xcf\x0bS\x96qR\x8c\xb6\xbf\xf9\xd9\xb3b\xe7F*\xa4\xdb\xc9\x9f\xf6[\xfck7\xfb2\xf7\xfe}\xcf\xfd\xf6\xbf\xe3]\x95\x87\x884o\x14O\r\xad\xcaEc{r\x88`\x9e&%%r\t \xa9\x03o9\xc6O$\x10\x18\xf1\x9d\x1f\xf8Bu_\xf9\xede\xff\x00}\xb7\xff\x00\x13]Q\x9cd\xae\x8d\xe5G\x06\xdf\xef/\x07\xdb\xfa\xb9\xd4k\x92J \x8b\xc9\x89\xa4um\xc0\x02\x14)\x1d\x18\x93\xc0\xc7\xbdy\xb3\xdd\xdd\xc2\xb7\x02\xe1\x94C\xf6o\xb4#Dw\xb4\x99$\x1cn\xc8\xca\xfc\xa5\xba\xf5\x1e\xb5\xb5\xe2\xaf\x1a\xc1\x042Cb\x92\\HW\xef*\x92\x06?OC\xd6\xb8y<A3\xe8\xfa\x85\xecbh\xd6\xdeH\xb8\x97\'\xe6$\x83\x8e\xdd\xfa\x8fQ\xeb^.-\xc6\xb5D\xe1\xaf\xe4i\x84\xc3\xd5\xa7O\x9aJ\xc9\x9b\xd77mq\x1bG\x9c\xbc\x17H\xe3\x8e9\x000<`\x8d\xaex\xcfc\xe9X^=\x9e\xda\xe7C\xb6y\xa4(\x89>\xc8\xc0\xc8\x1b\xca0\x0c\xd8>\x98\xe7\x1dG\xb9\xack-m\xf5 Y_\x13\x81\x86Y0\x00u9F\xfa\x11\x95ls\xd3\x18\xebSx\x9d\xdd\xb4\x99\xf6\xc7\x1c\xa2\tR\xe8,\x8b\xb8\x18\xcepq\xdb\x9c\x83\x9cp\x0fj\xc2\x8c\'N\xb4c#v\x94]\xdfC\x90\x1al\xd6\xf3\xc14n&\x10a\xd8FD\xa9\x8c\xee\xc3\x1e\x98\xc7\\\x8cu\xe3\x83Oh\xed\xafn\x1eb\x02\xc8K\xb7\x99\x1a\xacJI#\x92\xb9 \x01\x9e\x8a=ES\xb2\xd4r\x0f\x90\x88\x19\x95\x91\xd5Qy\x18\x03;\x9b\xd7\xd3\x1c~&\xa4\x9e\xed\xadd\xcd\xc5\x8a\x1b|\xf9\x91\xc2\xdb\x95;g\x95 \xf4\xc089\xe7\xb7oe\xa9\xb7g\xb8\x9chJ\x1c\xd6\xd3\xf06\xc6\xa1\x05\xacN\xdat\xf1\xc4\x92H\xa08\x8b\xcc\x01\x9599e\xca\x82\xdb\x8f\x1d8\xe7\x8a\xed\x7f\xe1/\x97\xfe\x83W\xdf\xf8\x0c\x7f\xf8\xe5y\x9e\x95\x04z\x84\x90\xc2\xf3G\xb4\xfc\xca\xb1\x92\x19Opr9\xcf\xe3\xd3\xadv_\xf0\x8fC\xfd\xc7\xff\x00\xbf\xa7\xfck\x87\x13*P\x92S\xdc\xea\xa1JUax\xda\xc7\xab\xf8\x97\xc3\xd2\xeb2\xc5s\x04\x89\xbd\x13o\x96\xdcg\xa9\xe0\xfa\xf2k\x89\xb9\xf0V\xa3\xe6\xaf\x9dc\xba<\x82\xeb\xb3\x7f\xe5\x8c\xd1E^;\t\x18\xc9\xd4\x8bi\x9e^\x0f4\xadN\x92\x86\x8d\x14\xb5O\x03\xdd\\\x1f:\xde\xda\xee\x19@\xc0dF\xc0\x1f\x88\xe4U{%\xbc\xd2\xe5\xfb\'\x88bH\xe3\xc3\x08&*\x0bc\x8d\xc0\xa8\xfe\x13\x90N{\xe4v\xc2\x94W\r;\xca\x9f,\x9d\xce\x87\x8c\x95o\x8a(\xc9\xd4|\x05\x03y\x97\x9a=\xf8\x95\x18\x9d\xd1,\x8a\xeb\x9c\xf4\xdcH\xc68\x1d\xcf\xb9\xac4\x86\xe2\t>\xcf\xa8\x15a\x06\n\xae\xef0\x03\x9fO\xc4\x9e\xbe\xbf\x81Et\xd2\xafRW\x8c\x9d\xeckEZ\\\x8bc\xba\xf0\xa7\x83b\xd4\xb5e\x96+E\x8a CHW?"\xfdOs\xfa\xfeu\xeb\xff\x00\xd8Zg\xfc\xf8\xdb\xff\x00\xdf\xa1\xfe\x14Q]X*J\xa49\xe7\xabg\x0eg\x88\x9a\xae\xe9\xc7E\x1d\x8f\xff\xd9'  # noqa


def test_make_thumbnail():
    path = Path(__file__)
    logo = path.parent.parent / 'data' / 'images' / 'splash.png'

    thumbnail = make_thumbnail(str(logo))
    x, y = thumbnail.size
    assert y == 127
    assert x == 256

    thumbnail = make_thumbnail(str(logo), ThumbnailSize.SMALL)
    x, y = thumbnail.size
    assert y == 63
    assert x == 128


def test_image_utils():
    image = bytes_to_image(IMAGE)
    bytes_ = image_to_bytes(image)

    image2 = bytes_to_image(bytes_)
    assert ImageChops.difference(image, image2).getbbox() == (0, 0, 57, 40)


def test_bytes_to_pixbuf():
    pixbuf = bytes_to_pixbuf(IMAGE)
    assert isinstance(pixbuf, Pixbuf)


def test_pixbuf_to_image():
    pixbuf = bytes_to_pixbuf(IMAGE)
    image = pixbuf_to_image(pixbuf)
    assert isinstance(image, Image.Image)


def test_image_to_pixbuf():
    image = bytes_to_image(IMAGE)
    pixbuf = image_to_pixbuf(image)
    assert isinstance(pixbuf, Pixbuf)

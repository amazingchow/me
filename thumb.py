# -*- coding: utf-8 -*-
from PIL import Image


def get_thumb():
    in_file = "./me.jpeg"
    out_file = "./me_thumbnail.jpeg"
    try:
        im = Image.open(in_file)
        size = 128, 128
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(out_file, "JPEG")
    except IOError:
        print("cannot create thumbnail for '%s'" % in_file)


if __name__ == "__main__":
    get_thumb()

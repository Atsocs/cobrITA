import os
import sys

import pytmx

from definitions import MAPS_DIR
from maps_utils.utils import translate

traduccion = {'2': '_', '1': '1'}


def check_width(lines, line_width):
    for ln in lines:
        assert len(ln) == line_width


def main(name):
    tmxpath = os.path.join(MAPS_DIR, 'tmx', name + '.tmx')
    tiled_map = pytmx.TiledMap(tmxpath)
    w, h = tiled_map.width, tiled_map.height
    start = 5
    end = start + h
    with open(tmxpath) as f:
        good_lines = f.readlines()[start:end]
    good_lines = [ln.strip('\n').replace(',', '') for ln in good_lines]
    good_lines = [translate(ln, traduccion) for ln in good_lines]
    check_width(good_lines, w)

    filename = os.path.join(MAPS_DIR, 'txt', name + '.txt')
    f = open(filename, "w+")
    f.write('\n'.join(good_lines))
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])

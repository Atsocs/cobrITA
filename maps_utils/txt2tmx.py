import os
import sys

from definitions import MAPS_DIR
from utils import translate

traduccion = {'1': '1', '_': '2'}

start = """<?xml version="1.0" encoding="UTF-8"?>
<map version="1.2" tiledversion="1.3.2" orientation="orthogonal" renderorder="right-down" compressionlevel="0" width="20" height="20" tilewidth="32" tileheight="32" infinite="0" nextlayerid="2" nextobjectid="1">
 <tileset firstgid="1" source="../tiles/tiles.tsx"/>
 <layer id="1" name="Camada de Tiles 1" width="20" height="20">
  <data encoding="csv">"""
end = """</data>
 </layer>
</map>
"""


def main(name):
    txtpath = os.path.join(MAPS_DIR, 'txt', name + '.txt')
    with open(txtpath) as f:
        middle = f.readlines()
    middle = [translate(ln, traduccion) for ln in middle]
    middle = [''.join([c + ',' for c in ln.strip('\n')]) for ln in middle]
    middle[-1] = middle[-1][:-1]
    middle = '\n'.join(middle)

    filename = os.path.join(MAPS_DIR, 'tmx', name + '.tmx')
    f = open(filename, "w+")
    f.write('\n'.join([start, middle, end]))
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])

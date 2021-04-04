import os
import random
import sys

# Creates random maps in the specified file of size w x h

# Example usages in the terminal:
# 1. Creates a map named "map_name.txt":
# $ python3 create_random_txt_map.py map_name
# 2. Creates maps named "a.txt", "b.txt", ... "z.txt":
# $ python3 create_random_txt_map.py {a..z}

from definitions import MAPS_DIR, L


def main(filenames):
    for filename in filenames:
        path = os.path.join(MAPS_DIR, 'txt', filename + '.txt')
        c = '_1'
        w = h = L
        m = [''.join([random.choice(c) for x in range(w)]) for y in range(h)]
        f = open(path, "w+")
        f.write('\n'.join(m))
        f.close()


if __name__ == '__main__':
    main(sys.argv[1:])

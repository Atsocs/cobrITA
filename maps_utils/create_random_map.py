import sys

from maps_utils import create_random_txt_map, txt2tmx


def main(name):
    create_random_txt_map.main([name])
    txt2tmx.main(name)


if __name__ == '__main__':
    main(sys.argv[1])

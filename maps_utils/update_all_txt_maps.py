import os

import tmx2txt
from maps_utils.meta_utils import erase_folder
from definitions import MAPS_DIR

TXT_DIR = os.path.join(MAPS_DIR, 'txt')
TMX_DIR = os.path.join(MAPS_DIR, 'tmx')

erase_folder(TXT_DIR)

# create new txts
for name in os.listdir(TMX_DIR):
    trimmed = name[:-4]
    tmx2txt.main(trimmed)

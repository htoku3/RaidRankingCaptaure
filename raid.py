from time import sleep
import shutil
import glob
import os

SCREEN_SHOT_DIR = os.environ["USERPROFILE"] + u"\\Documents\\ミストレレイド"
INIT_IDX = len(glob.glob(SCREEN_SHOT_DIR + "\capture*.png"))
MAX_IDX = 999

match = None
# Search mst window
while match is None:
    for id in range(Screen.getNumberScreens()):
        try:
            match = Screen(id).find(Pattern("1651561551777.png").similar(0.95))
        except FindFailed:
            pass

print(match)
mst_app = Region(match.x - 31, match.y - 15, 1134, 638)

# Make directory if not exists.
if not os.path.exists(SCREEN_SHOT_DIR):
    os.makedirs(SCREEN_SHOT_DIR)

# Take screen shots
idx = INIT_IDX
while idx < MAX_IDX:
    match = None
    while match is None:
        try:
            match = mst_app.find(Pattern("1651552265746.png").exact())
        except FindFailed:
            sleep(0.2)
    print(match)
    sleep(0.8)
    tmpfile =  capture(mst_app)
    shutil.move(tmpfile, SCREEN_SHOT_DIR + "\capture_{:03}.png".format(idx))
    sleep(4)
    idx += 1    

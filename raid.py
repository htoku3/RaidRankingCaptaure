from time import sleep
import shutil
import glob
import os

SCREEN_SHOT_DIR = os.environ["USERPROFILE"] + u"\\Documents\\ミストレレイド"
INIT_IDX = len(glob.glob(SCREEN_SHOT_DIR + "\capture*.p*"))
MAX_IDX = 999

match = None
# Search mst window
print("Search \"BOSS\" in the screens.")
Screen.showMonitors()
while match is None:
    for id in range(Screen.getNumberScreens()):
        try:
            match = Screen(id).find(Pattern("1651561551777.png").similar(0.95))
            print("Found \"BOSS\" in screen {}.".format(id))
            print("The position of the window is set. please do not move window.")
        except FindFailed:
            sleep(0.5)

mst_app = Region(match.x - 46, match.y - 18, 1135, 638)

# Make the directory if doesn't exist.
if not os.path.exists(SCREEN_SHOT_DIR):
    os.makedirs(SCREEN_SHOT_DIR)

print("Start capturing results.")
# Take screen shots
idx = INIT_IDX
while idx < MAX_IDX:
    match = None
    while match is None:
        try:
            match = mst_app.find(Pattern("1651552265746.png").exact())
        except FindFailed:
            sleep(0.2)
    print("\"1st\" is found ({}). Capturing screen".format(match))
    sleep(0.8)
    tmpfile =  capture(mst_app)
    shutil.move(tmpfile, SCREEN_SHOT_DIR + "\capture_{:03}.png".format(idx))
    sleep(4)
    idx += 1    

##############################
# IGNORE this section        #
##############################
# not related to core part, can be safely ignored
from preface import *
image_stim = visual.ImageStim(win=win)

##############################
# copy below                 #
##############################

##############################
# before experiment          #
##############################
import numpy as np
##############################
# start experiment           #
##############################

##############################
# before routine             #
##############################

n_frames = 240
speed: int = 30
frames = []

first_frame = np.linspace(-1, 1, 1920*1080).reshape(1080, 1920)
first_frame *= np.pi
np.sin(first_frame, out=first_frame)
frames.append(first_frame)
for i in range(1, n_frames):
    frame = np.roll(first_frame, i*speed, axis=0)
    frames.append(frame)
win.recordFrameIntervals = True
win.fps()
##############################
# each frame                 #
##############################
image_stim.setImage(frames[frameN], )
if frameN >= n_frames - 1:
    print("FPS: ", win.fps())

##############################
# after routine              #
##############################

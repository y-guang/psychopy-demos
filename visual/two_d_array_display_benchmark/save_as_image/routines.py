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

n_frames = 240
speed: int = 30
frames = []

first_frame = np.linspace(0, 1, 1920*1080).reshape(1080, 1920)
first_frame *= np.pi
np.sin(first_frame, out=first_frame)
first_frame *= 255
first_frame = first_frame.astype(np.uint8)
frames.append(first_frame)
for i in range(1, n_frames):
    frame = np.roll(first_frame, i*speed, axis=0)
    frames.append(frame)

# save as gif
from PIL import Image
images = []
for frame in frames:
    image = Image.fromarray(frame, mode='L')
    images.append(image)
images[0].save('rolling_sine_wave.gif',
               save_all=True,
               append_images=images[1:],
               duration=1000//120,
               loop=0,
               optimize=False)

##############################
# before routine             #
##############################

win.recordFrameIntervals = True
win.fps()
##############################
# each frame                 #
##############################

if frameN >= n_frames - 1:
    print("FPS: ", win.fps())

##############################
# after routine              #
##############################

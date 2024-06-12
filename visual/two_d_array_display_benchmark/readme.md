screen size image can not be present stably in terms of fps.

Not work attempts:
- with numpy only. ~40fps.
- PIL lib. convert to PIL Image deteriorate performance.
- uint8 array. Not supported by psychopy ImageStim.setImage.
- preload all frame images as ImageStim. 
  - better fps (achieves >60 on my laptop), but not stable.
  - spend much time to load the images.
  - spend >10G memory.
- even not work when save as gif, when the image size become big.
# Image_processing_Selective_Coloring_effect
This effect is usually used in tracking applications
(finding the red object in a scene and tracking it) or in movies. The aim of selective coloring is highlighting a specific range of colors , while keeping the background in grayscale

When you run the selective_coloring_effect.py, it shows two video windows: 'frame' window shows color video-streaming, 'result' window shows gray video-streaming with a color you click on 'frame' window

The main concept is to track the HUE parameter of the pixel of a frame and apply mask with tolerance value. Applying kernel filter is optional and was included for testing. Version of cv2: 4.5.1

Below you can see the result: 
[![Watch the video](https://github.com/RustamChib/Image_Processing_Selective_Coloring_effect/blob/main/result.gif)](https://youtu.be/tIJqNCWD39o)


For more qualitative representation click on the GIF, it will redirect to the youtube. 

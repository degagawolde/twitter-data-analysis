import matplotlib.pyplot as plt
import numpy as np

image = np.empty((1376, 960), np.uint16)

image.data[:] = open(
    '/Volumes/Untitled/img-2/image/BODYPART_Abdomen_AP_20210426111258/image.raw').read()

plt.imshow(image)



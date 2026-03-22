# dda_demo.py
import numpy as np
import matplotlib.pyplot as plt

def dda_line(x0,y0,x1,y1,img):
    dx = x1-x0; dy = y1-y0
    steps = int(max(abs(dx),abs(dy)))
    if steps==0:
        img[int(round(y0)), int(round(x0))] = 0
        return img
    x_inc = dx/steps; y_inc = dy/steps
    x,y = x0,y0
    for _ in range(steps+1):
        img[int(round(y)), int(round(x))] = 0
        x += x_inc; y += y_inc
    return img

w,h = 200,200
img = 255*np.ones((h,w), dtype=np.uint8)
img = dda_line(20,30,170,150,img)
plt.imshow(img, cmap='gray', origin='upper'); plt.axis(); plt.grid(); plt.show()

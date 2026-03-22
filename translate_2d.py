# translate_2d.py
import numpy as np

# point set (square)
pts = np.array([[0,0,1],[1,0,1],[1,1,1],[0,1,1]]).T  # homogeneous coordinates (3xN)
tx, ty = 2.5, -1.0
T = np.array([[1,0,tx],[0,1,ty],[0,0,1]])
translated = T @ pts
print("Original:\n", pts[:2,:].T)
print("Translated:\n", translated[:2,:].T)

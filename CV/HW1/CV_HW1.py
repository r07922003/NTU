# coding: utf-8

from PIL import Image
import numpy as np

def up_side_down(array):
    up_side_down=[]
    for i in range(len(array)-1,-1,-1):
        up_side_down.append(array[i])
    up_side_down=np.array(up_side_down)
    up_side_down = Image.fromarray(up_side_down)
    return up_side_down

def right_side_left(array):
    right_side_left=[]
    for i in range(len(array)):
        right_side_left.append([])
        for j in range(len(array)-1,-1,-1):
            right_side_left[i].append(array[i][j])
    right_side_left=np.array(right_side_left)
    right_side_left = Image.fromarray(right_side_left)
    return right_side_left
def diagonally_mirrored(array):
    output=[]
    diagonally_mirrored=np.array(right_side_left(array))
    for i in  range(len(diagonally_mirrored)-1,-1,-1):
        output.append(diagonally_mirrored[:,i])
    output=np.array(output)
    output = Image.fromarray(output)
    return output

lena = Image.open("lena.bmp")
array=np.array(lena)
a=up_side_down(array)
b=right_side_left(array)
c=diagonally_mirrored(array)
a.show(),b.show(),c.show()


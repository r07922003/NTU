
# coding: utf-8

# In[158]:


from PIL import Image,ImageDraw
import numpy as np

u_v=[1,1]
k=0.04
box_size = 1
image_name = 'pan/imgs/prtn00.jpg'
save_name = 'change.jpg'
def shifted_intensity(pixel,u,v,index_x,index_y,box_size):
    array=np.zeros((box_size*2+1,box_size*2+1))
    for i in range(-1*box_size,box_size+1):
        for j in range(-1*box_size,box_size+1):
            try:
                array[i+2,j+2] = pixel[index_x+i+u,index_y+j+v] - pixel[index_x+i,index_y+j]
            except:
                pass
    return array
"""
def shifted_intensity(pixel,u,v):
    array = np.zeros(shape=(width,height))
    if u>=0 and v>=0:
        for i in range(width-u):
            for j in range(height-v):
                array[i,j] = np.array(pixel[i+u,j+v])-np.array(pixel[i,j])
    elif u<0 and v>=0:
        for i in range(-1*u,width):
            for j in range(height-v):
                array[i,j] = np.array(pixel[i+u,j+v])-np.array(pixel[i,j])
    elif u>=0 and v<0:
        for i in range(width-u):
            for j in range(-1*v,height):
                array[i,j] = np.array(pixel[i+u,j+v])-np.array(pixel[i,j])
    else:
        for i in range(-1*u,width):
            for j in range(-1*v,height):
                array[i,j] = np.array(pixel[i+u,j+v])-np.array(pixel[i,j])
    return array
"""
def window_function(box_size):
    window_function=np.zeros((box_size*2+1,box_size*2+1))
    array = []
    for x in range(-1*box_size,1):
        for y in range(-1*box_size,1):
            window_function[x+box_size][y+box_size] = (x+2)**2 + (y+2)**2
    for size in range(1,box_size+1):
        window_function[box_size+size] = window_function[box_size-size]
    for size in range(1,box_size+1):
        window_function[:,box_size+size] = window_function[:,box_size-size]
    sigma = np.std(window_function)**2
    window_function = np.exp(((-1)*window_function)/(2*sigma))
    """
    sigma = np.std(array)
    w = np.zeros(np.shape(array))
    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            try:
            w[x,y] = np.exp(-1*( (x**2+y**2) / (2*(sigma**2)) ))
    """
    return window_function

def non_max_value_suppression(pixel,R_array,box_size):
    array=np.zeros(R_array.shape)
    for i in range(width):
        for j in range(height):
            temp = []
            for x in range(-1*box_size,box_size+1):
                for y in range(-1*box_size,box_size+1):
                    try:
                        pixel[i+x,j+y]
                        temp.append(R_array[i+x,j+y])
                    except:
                        pass
            if R_array[i,j] == np.max(temp):
                array[i,j] = R_array[i,j]
            else:
                array[i,j] = 0
    return array



def main():
    print("Harris corner detector")
    image = Image.open(image_name).convert("L")
    array = np.array(image)
    height = image.height
    width = image.width
    pixel = image.load()
    R_array = np.zeros(shape=(width,height))
    w = window_function(box_size)
    plot_size = 2
    image.close()
    for i in range(width):
        for j in range(height):
            Ix = shifted_intensity(pixel,0,1,i,j,box_size)
            Iy = shifted_intensity(pixel,1,0,i,j,box_size)
            A = w*Ix*Ix
            B = w*Iy*Iy
            C = w*Ix*Iy
    #E_uv = A*u_v[0]*u_v[0] + 2*C*u_v[0]*u_v[1] + B*u_v[1]*u_v[1]
            M = np.array([[np.sum(A),np.sum(C)],[np.sum(C),np.sum(B)]])
            R = np.linalg.det(M) - k*(np.trace(M)**2)
            R_array[i,j] = R
    NMVS = non_max_value_suppression(pixel,R_array,box_size)
    result = NMVS
    #result = R_array

    threshlod = 7000000
    new_array = np.zeros(result.shape)
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if NMVS[i,j] <= threshlod:
                new_array[i,j] = 0
            else:
                new_array[i,j] = 255
    image = Image.open(image_name)
    draw = ImageDraw.Draw(image)

    for i in range(R_array.shape[0]):
        for j in range(R_array.shape[1]):
            if new_array[i,j]==0:
                pass
                #draw.point((i,j),fill='black')
            else:
                #pass
                draw.point((i,j),fill='red')
                """
                for x in range(-1*plot_size,plot_size+1):
                    draw.point((i+x,j),fill='red')
                    draw.point((i,j+x),fill='red')
                """
    image.save(save_name)
    image.close()
main()


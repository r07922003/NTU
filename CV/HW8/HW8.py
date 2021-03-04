from PIL import Image, ImageDraw
import numpy as np

def Gaussian_noise(img, amp):
    pixel = img.load()
    Gaussian_noise_img = Image.new(img.mode, img.size)
    
    for i in range(0,512,1):
        for j in range(0,512,1):
            Gaussian_noise_img.putpixel((i,j),int( pixel[i,j] + amp * np.random.normal(0,1)) ) 
            
    return Gaussian_noise_img

def salt_and_pepper_noise(img, threshold):
    pixel = img.load()
    salt_and_pepper_noise_img = Image.new(img.mode, img.size)
    
    for i in range(0,512,1):
        for j in range(0,512,1):
            rand = np.random.sample()
            if rand < threshold:
                salt_and_pepper_noise_img.putpixel((i,j),0)
            elif rand > 1 - threshold:
                salt_and_pepper_noise_img.putpixel((i,j),255)
            else:
                salt_and_pepper_noise_img.putpixel((i,j),pixel[i,j])
    return salt_and_pepper_noise_img

def box_and_median_filter(img, box_size):
    pixel = img.load()
    img_box = Image.new(img.mode, img.size)
    img_median = Image.new(img.mode, img.size)
    
    x_start = int(box_size/2)
    y_start = int(box_size/2)
    for i in range(0,512,1):
        for j in range(0,512,1):
            box_collect = []
            for x in range(0,box_size,1):
                for y in range(0,box_size,1):
                    try:
                        box_collect.append( pixel[i+x-x_start, j+y-y_start] )
                    except:
                        pass
            img_box.putpixel((i,j) , int(np.mean(np.array(box_collect))) )
            img_median.putpixel((i,j) ,int( np.median(np.array(box_collect))) )

    return img_box, img_median

def dilation(img, kernel):
    pixel = img.load()
    coulmn,row=img.size
    img_new = Image.new(img.mode, img.size)

    for i in range(0,coulmn,1):
        for j in range(0,row,1):
            if pixel[i,j] > 0:
                dil_pix_list = []
                for y in range(-2,3,1):
                    for x in range(-2,3,1):
                        if kernel[y+2,x+2] == 1:
                            if (i+x < coulmn) and (j+y < row) and (i+x >= 0) and (j+y >= 0):
                                dil_pix_list.append(pixel[i+x,j+y])
                
                max_pix = max(dil_pix_list)
                for y in range(-2,3,1):
                    for x in range(-2,3,1):
                        if kernel[y+2,x+2] == 1:
                            if (i+x < coulmn) and (j+y < row) and (i+x >= 0) and (j+y >= 0):
                                img_new.putpixel((i+x,j+y),max_pix)
    return img_new

def erosion(img, kernel):
    pixel = img.load()
    coulmn,row=img.size
    img_new = Image.new(img.mode, img.size )
    for i in range(0,coulmn,1):
        for j in range(0,row,1):
            ero_flag = True
            ero_pix_list = []
            for y in range(-2,3,1):
                for x in range(-2,3,1):
                    if kernel[y+2,x+2] == 1:
                        if (i+x < coulmn) and (j+y < row) and (i+x >= 0) and (j+y >= 0):
                            ero_pix_list.append(pixel[i+x,j+y])
                            if pixel[i+x,j+y] == 0:
                                ero_flag = False
                        else:
                            ero_flag = False
            
            min_pix = min(ero_pix_list)
            if ero_flag :
                img_new.putpixel((i,j),min_pix)
                
    return img_new

def opening(img, kernel):
    img_ero = erosion(img, kernel)
    img_new = dilation(img_ero, kernel)

    return img_new

def closing(img, kernel):
    img_dil = dilation(img, kernel)
    img_new = erosion(img_dil, kernel)

    return img_new

def SNR_calculate(img_orig, img_proc):
    pixel_orig = img_orig.load()
    pixel_proc = img_proc.load()
    
    orig_array = np.array((512,512))
    proc_array = np.array((512,512))
    mu = 0
    mu_n = 0
    VS = 0
    VN = 0
    for i in range(0,512,1):
        for j in range(0,512,1):
            mu += pixel_orig[i,j]
            mu_n += pixel_proc[i,j] - pixel_orig[i,j]

    mu = mu / (512*512)
    mu_n = mu_n / (512*512)

    for i in range(0,512,1):
        for j in range(0,512,1):
            VS += (pixel_orig[i,j] - mu) ** 2
            VN += (pixel_proc[i,j] - pixel_orig[i,j] - mu_n) ** 2

    VS = VS / (512*512)
    VN = VN / (512*512)

    SNR = 20 * np.log10( np.sqrt(VS) / np.sqrt(VN) )
    return SNR

def image_processing(img, file_name):
    img_box_3 , img_median_3 = box_and_median_filter(img, 3)
    img_box_5 , img_median_5 = box_and_median_filter(img, 5)

    kernel_array = np.array([[0,1,1,1,0],
                             [1,1,1,1,1],
                             [1,1,1,1,1],
                             [1,1,1,1,1],
                             [0,1,1,1,0]])
    img_open = opening(img, kernel_array)
    img_close = closing(img, kernel_array)
    img_close_open = opening(img_close, kernel_array)
    img_open_close = closing(img_open, kernel_array) 

    img_box_3.save('./processed/' + file_name + '_box_3.bmp')
    img_box_5.save('./processed/' + file_name + '_box_5.bmp')
    img_median_3.save('./processed/' + file_name + '_median_3.bmp')
    img_median_5.save('./processed/' + file_name + '_median_5.bmp')
    img_close_open.save('./processed/' + file_name + '_close_open.bmp')
    img_open_close.save('./processed/' + file_name + '_open_close.bmp')

    print ( file_name + "_box_3 : " + str( SNR_calculate(img, img_box_3) ))
    print ( file_name + "_box_5 : " + str( SNR_calculate(img, img_box_5) ))
    print ( file_name + "_median_3 : " + str( SNR_calculate(img, img_median_3) ))
    print ( file_name + "_median_5 : " + str( SNR_calculate(img, img_median_5) ))
    print ( file_name + "_close_open : " + str( SNR_calculate(img, img_close_open) ))
    print ( file_name + "_open_close : " + str( SNR_calculate(img, img_open_close) ))


lena=Image.open("lena.bmp")

img_noise = Gaussian_noise(lena, 10)
img_noise.save('./noised/Gaussian_10.bmp')
image_processing(img_noise, 'GS_10')

img_noise = Gaussian_noise(lena, 30)
img_noise.save('./noised/Gaussian_30.bmp')
image_processing(img_noise, 'GS_30')

img_noise = salt_and_pepper_noise(lena, 0.05)
img_noise.save('./noised/Salt_and_Pepper_005.bmp')
image_processing(img_noise, 'S&P_005')

img_noise = salt_and_pepper_noise(lena, 0.1)
img_noise.save('./noised/Salt_and_Pepper_01.bmp')
image_processing(img_noise, 'S&P_01')
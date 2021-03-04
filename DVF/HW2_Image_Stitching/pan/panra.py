import numpy as np
import glob
import cv2

def loadImg():
	fileList = glob.glob('./*.jpg')
	imgList = list()
	for f in fileList:
		imgList.append(cv2.imread(f, 0))
	return imgList

#  x1 x2 x3
#  x4 x5 x6
#  x7 x8 x9
def featureDescription(img, x, y):
	FD = list()
	h, w = img.shape
	if y == 0:
		if x == 0:
			FD = [	0, 0,         0,
					0, img[y,x],  img[y,x+1],
					0, img[y+1,x],img[y+1,x+1]]
		elif x == w-1:
			FD = [	0,			 0,			 0,
					img[y,x-1],  img[y,x], 	 0,
					img[y+1,x-1],img[y+1,x], 0]
		else:
			FD = [	0, 			  0, 		  0,
					img[y,x-1],   img[y,x],   img[y,x+1],
					img[y+1,x-1], img[y+1,x], img[y+1,x+1]]
	elif y == h-1:
		if x == 0:
			FD = [	0,	img[y-1,x],	img[y-1,x+1],
					0,	img[y,x],	img[y,x+1],
					0,	0,			0]
		elif x == w-1:
			FD = [	img[y-1,x-1],	img[y-1,x],	0,
					img[y,x-1],		img[y,x],	0,
					0,				0,			0]			
		else:
			FD = [	img[y-1,x-1],	img[y-1,x],	img[y-1,x+1],
					img[y,x-1],		img[y,x],	img[y,x+1],
					0,				0,			0]
	else:
		if x == 0:
			FD = [	0,	img[y-1,x],	img[y-1,x+1],
					0,	img[y,x],	img[y,x+1],
					0,	img[y+1,x],	img[y+1,x+1]]
		elif x == w-1:
			FD = [	img[y-1,x-1],	img[y-1,x],	0,
					img[y,x-1],		img[y,x],	0,
					img[y+1,x-1],	img[y+1,x],	0]
		else:
			FD = [	img[y-1,x-1],	img[y-1,x],	img[y-1,x+1],
					img[y,x-1],		img[y,x],	img[y,x+1],
					img[y+1,x-1],	img[y+1,x],	img[y+1,x+1]]
	return FD

def harrisCorner(img, k=0.04, windowSize=2, threshold=500000):
	dy,dx = np.gradient(img)
	Ixx = dx**2
	Ixy = dy*dx
	Iyy = dy**2
	h, w = img.shape

	cornerList = list()
	newImg = img.copy()
	offset = windowSize/2

	for y in range(offset, h-offset):
		for x in range(offset, w-offset):
			WIxx = Ixx[y-offset:y+offset+1, x-offset:x+offset+1].sum()
			WIxy = Ixy[y-offset:y+offset+1, x-offset:x+offset+1].sum()
			WIyy = Iyy[y-offset:y+offset+1, x-offset:x+offset+1].sum()

			det = (WIxx * WIyy) - (WIxy**2)
			trace = WIxx + WIyy
			r = det - k*(trace**2)

			if r > threshold:
				#print x, y, r
				cornerList.append([x, y, r])
	cornerList.sort(key=lambda val:val[2], reverse=True)
	return cornerList

def main():
	# load images
	imgList = loadImg()

	# feature detection
	cnt=0
	FD_pre = list()
	for img in imgList:
		FD_next = list()
		temp = img.copy()
		cornerList = harrisCorner(img)
		for idx in range(len(cornerList)/40):
			x, y, _ = cornerList[idx]
			FD_next.append([x, y, featureDescription(img, x, y)])
			temp[y,x] = 128
		cv2.imwrite('out_'+str(cnt)+'.jpg', temp)
		cnt += 1

		# feature matching
		if len(FD_pre) == 0:
			FD_pre = FD_next
			continue
		print len(FD_pre), len(FD_next)
		print FD_pre
		print FD_next

	# image matching

	# blending



if __name__ == "__main__":
	main()

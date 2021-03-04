import random
import matplotlib.pyplot as plt
import numpy as np
import math
import cv2
import exifread

IMG_LIST = [
	"IMG_2605.JPG",
	"IMG_2606.JPG",
	"IMG_2607.JPG",
	"IMG_2608.JPG",
	"IMG_2609.JPG",
	"IMG_2610.JPG",
	"IMG_2611.JPG",
	"IMG_2618.JPG",
	"IMG_2619.JPG"]
#exposure_times = np.array([1/640., 1/320., 1/200., 1/100., 1/50., 1/25., 1/10., 1/4., 1/2.], dtype=np.float32)
exposure_times = np.array([], dtype=np.float32)

def getExposureTime(img):
	with open(img) as fp:
		temp = str(exifread.process_file(fp)['EXIF ExposureTime']).split('/')
		return float(temp[0])/float(temp[1])

def loadImgs():
	imgB = [] ;imgG = [] ;imgR = []
	global exposure_times

	print("| %-20s | %-15s |" % ("PictureName", "ExposureTime"))
	for img in IMG_LIST:
		imgT = cv2.imread(img)
		imgB.append(imgT[:,:,0])
		imgR.append(imgT[:,:,1])
		imgG.append(imgT[:,:,2])
		exposure_times = np.append(exposure_times, getExposureTime(img))
		print("| %-20s | %-15f |" % (img, exposure_times[-1]))
	return imgB, imgR, imgG

def getPixelVal(Img, Map):
	valMap = []
	for img in Img:
		tmp = list()
		for i in Map:
			tmp.append(img[int(i%img.shape[0]), int(i/img.shape[0])])
		valMap.append(tmp)
	return valMap

def genCompPixel(imgB, imgG, imgR):
	sampleMap = []
	sampleNum = 100

	sampleImg = imgR[len(imgR)//2]
	size = sampleImg.shape[0] * sampleImg.shape[1]
	while len(sampleMap) < sampleNum:
		i = random.randint(0, size - 1)
		sampleMap.append(i)

	return getPixelVal(imgB,sampleMap), getPixelVal(imgG,sampleMap), getPixelVal(imgR,sampleMap)

def CalCRC(Z, B, l, w):
	n = 256
	A = np.zeros((np.size(Z,1)*np.size(Z,0)+n+1, n+np.size(Z,1)), dtype=np.float32)
	b = np.zeros((np.size(A,0), 1), dtype=np.float32)

	# Include the data-fitting equations
	k = 0
	for i in range(np.size(Z,1)):
		for j in range(np.size(Z,0)):
			wij = w[Z[j][i]]
			A[k][Z[j][i]] = wij; A[k][n+i] = -wij; b[k] = wij*B[j]
			k += 1

	# Fix the curve by setting its middle value to 0
	A[k][128] = 1
	k += 1

	# Include the smoothness equations
	for i in range(n - 1):
		A[k][i] = l*w[i+1]; A[k][i+1] = -2*l*w[i+1]; A[k][i+2] = l*w[i+1]
		k += 1

	# Solve the system using SVD
	x = np.dot(np.linalg.pinv(A),b)
	g = x[0:n]
	lE = x[n:np.size(x, 0)]

	return g

def genRadMap(imgList, g, B, w):
	imgShape = imgList[0].shape
	imgRadianceMap = np.zeros(imgList[0].shape, dtype=np.float64)

	numImages = len(imgList)
	for i in range(imgShape[0]):
		for j in range(imgShape[1]):
			gz = list()
			wz = list()

			for k in range(0, numImages):
				gz.append(g[imgList[k][i,j]][0])
				wz.append(w[imgList[k][i,j]])

			gz = np.asarray(gz)
			wz = np.asarray(wz)
			if np.sum(wz) > 0:
				imgRadianceMap[i, j] = np.sum(wz*(gz-B)/np.sum(wz))
			else:
				imgRadianceMap[i, j] = gz[numImages//2]-B[numImages//2]
	return imgRadianceMap

def drawCRC(crcB, crcG, crcR):
	plt.figure()
	plt.plot(crcB, range(256), 'blue')
	plt.plot(crcG, range(256), 'green')
	plt.plot(crcR, range(256), 'red')
	plt.ylabel('pixel value Z')
	plt.xlabel('log exposure X')
	plt.savefig('CRC.png')

def main():
	img = cv2.imread(IMG_LIST[0])
	shape = img.shape
	width = shape[0]
	height = shape[1]

	imgListB, imgListG, imgListR = loadImgs()
	z_b, z_g, z_r = genCompPixel(imgListB, imgListG, imgListR)

	B = [math.log(e) for e in exposure_times]
	w = [z if z <= 127 else 255 - z for z in range(256)]

	# calculate Camera Response Curve
	L = 50
	crcB = CalCRC(z_b, B, L, w)
	crcG = CalCRC(z_g, B, L, w)
	crcR = CalCRC(z_r, B, L, w)
	blueCurve = np.exp(genRadMap(imgListB, crcB, B, w))
	greenCurve = np.exp(genRadMap(imgListG, crcG, B, w))
	redCurve = np.exp(genRadMap(imgListR, crcR, B, w))
	drawCRC(crcB, crcG, crcR)

	hdr = np.zeros(shape, 'float32')
	hdr[..., 0] = np.reshape(blueCurve, (width, height))
	hdr[..., 1] = np.reshape(greenCurve, (width, height))
	hdr[..., 2] = np.reshape(redCurve, (width, height))

	cv2.imwrite('out.hdr', hdr)
	normalize = lambda zi: (zi - zi.min() / zi.max() - zi.min())
	ldr = normalize(np.log(hdr))
	cv2.imwrite('hdr_image.jpg', (ldr/ldr.max())*255)
	tonemapReinhard = cv2.createTonemapReinhard(1.5, 3, 0.5, 0.5)
	ldrReinhard = tonemapReinhard.process(hdr)
	cv2.imwrite("ldr-Reinhard.jpg", ldrReinhard * 255)

if __name__ == "__main__":
	main()

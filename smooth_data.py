import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.ndimage.filters import gaussian_filter1d

global l_shoulder_xs
global l_shoulder_ys
global l_shoulder_zs
global r_shoulder_xs
global r_shoulder_ys
global r_shoulder_zs
global l_elbow_xs
global l_elbow_ys
global l_elbow_zs
global r_elbow_xs
global r_elbow_ys
global r_elbow_zs
global l_hand_xs
global l_hand_ys
global l_hand_zs
global r_hand_xs
global r_hand_ys
global r_hand_zs

def blur(a):
    kernel = np.array([[1.0,2.0,1.0], [2.0,4.0,2.0], [1.0,2.0,1.0]])
    kernel = kernel / np.sum(kernel)
    arraylist = []
    for y in range(3):
        temparray = np.copy(a)
        temparray = np.roll(temparray, y - 1, axis=0)
        for x in range(3):
            temparray_X = np.copy(temparray)
            temparray_X = np.roll(temparray_X, x - 1, axis=1)*kernel[y,x]
            arraylist.append(temparray_X)

    arraylist = np.array(arraylist)
    arraylist_sum = np.sum(arraylist, axis=0)
    return arraylist_sum

def process_input():
	l_shoulder_xs = []
	l_shoulder_ys = []
	l_shoulder_zs = []
	r_shoulder_xs = []
	r_shoulder_ys = []
	r_shoulder_zs = []
	l_elbow_xs = []
	l_elbow_ys = []
	l_elbow_zs = []
	r_elbow_xs = []
	r_elbow_ys = []
	r_elbow_zs = []
	l_hand_xs = []
	l_hand_ys = []
	l_hand_zs = []
	r_hand_xs = []
	r_hand_ys = []
	r_hand_zs = []

	with open("sara_data.txt") as infile:
		for line in infile:
			if 'l_shoulder' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				l_shoulder_xs.append(x)
				l_shoulder_ys.append(y)
				l_shoulder_zs.append(z)
			if 'r_shoulder' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				r_shoulder_xs.append(x)
				r_shoulder_ys.append(y)
				r_shoulder_zs.append(z)
			if 'l_elbow' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6]) 
				l_elbow_xs.append(x)
				l_elbow_ys.append(y)
				l_elbow_zs.append(z)
			if 'r_elbow' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				r_elbow_xs.append(x)
				r_elbow_ys.append(y)
				r_elbow_zs.append(z)
			if 'l_hand' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				l_hand_xs.append(x)
				l_hand_ys.append(y)
				l_hand_zs.append(z)
			if 'r_hand' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				r_hand_xs.append(x)
				r_hand_ys.append(y)
				r_hand_zs.append(z)
	return l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, r_hand_xs, r_hand_ys, r_hand_zs



def main():
	l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, r_hand_xs, r_hand_ys, r_hand_zs = process_input()

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	xs = np.asarray(l_hand_xs)
	ys = np.asarray(l_hand_ys)
	zs = np.asarray(l_hand_zs)

	#ax.scatter(xs, ys, zs)

	#gussian filter
	blurred_elbow_xs = gaussian_filter1d(xs, sigma = 1)
	blurred_elbow_ys = gaussian_filter1d(ys, sigma = 1)
	blurred_elbow_zs = gaussian_filter1d(zs, sigma = 1)
	ax.plot(blurred_elbow_xs, blurred_elbow_ys, blurred_elbow_zs)


	#difference histogram
	diff_x = [0]
	diff_y = [0]
	diff_z = [0]

	for i in range(2, len(xs)-1):
		diff_x.append(xs[i] - xs[i-1])
		diff_y.append(ys[i] - ys[i-1])
		diff_z.append(zs[i] - zs[i-1])

	mean_x = np.mean(diff_x)
	mean_y = np.mean(diff_y)
	mean_z = np.mean(diff_z)

	print(mean_x)
	diff_xs = []
	diff_ys = []
	diff_zs = []

	for i in range(0, len(xs)-2):
		if diff_x[i] < mean_x:
			if diff_y[i] < mean_y:
				if diff_z[i] < mean_z:
					diff_xs.append(xs[i])
					diff_ys.append(ys[i])
					diff_zs.append(zs[i])



	



	#ax.plot(diff_xs, diff_ys, diff_zs)

	plt.show()






if __name__ == "__main__":
    main() 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.ndimage.filters import gaussian_filter1d
from pykalman import KalmanFilter


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

def claculate_point_and_velocity(xs, ys, zs):
	x_velocity = [[xs[0], 0]]
	y_velocity = [[ys[0], 0]]
	z_velocity = [[zs[0], 0]]
	time = 0.3
	for i in range(1, len(xs)-2):
		distance = np.sqrt(np.square(xs[i] - xs[i-1]) + np.square(ys[i]-ys[i-1]) + np.square(zs[i] - zs[i-1]))
		if time == 0:
			velocity = 0
		else:
			velocity = distance/time
		time = time + 0.03
		x_diff = xs[i] - xs[i-1]
		y_diff = ys[i] - ys[i-1]
		z_diff = zs[i] - zs[i-1]

		x_velocity.append([xs[i], velocity])
		y_velocity.append([ys[i], velocity])
		z_velocity.append([zs[i], velocity])

	return x_velocity, y_velocity, z_velocity


def apply_kalman(matrix):
	kf = KalmanFilter(initial_state_mean=0, n_dim_obs=2)
	print("applied KalmanFilter")

	return kf.smooth(matrix)[0]
	



def main():
	l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, r_hand_xs, r_hand_ys, r_hand_zs = process_input()

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	xs = np.asarray(l_shoulder_xs)
	ys = np.asarray(l_shoulder_ys)
	zs = np.asarray(l_shoulder_zs)

	x_velocity, y_velocity, z_velocity = claculate_point_and_velocity(xs, ys, zs)

	sm_x = np.squeeze(np.asarray(apply_kalman(x_velocity)))
	sm_y = np.squeeze(np.asarray(apply_kalman(y_velocity)))
	sm_z = np.squeeze(np.asarray(apply_kalman(z_velocity)))

	print(sm_x)

	ax.plot(sm_x, sm_y, sm_z)

	plt.show()








if __name__ == "__main__":
    main() 

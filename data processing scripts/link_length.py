import numpy as np
import pylab
import matplotlib.pyplot as plt
from pykalman import KalmanFilter

from scipy.ndimage.filters import gaussian_filter1d


def process_input():
	head_xs = []
	head_ys = []
	head_zs = []
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

	with open("andreea_rand1_rotated.txt") as infile:
		for line in infile:
			if 'head' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				head_xs.append(x)
				head_ys.append(y)
				head_zs.append(z)
			if 'r_shoulder' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				l_shoulder_xs.append(x)
				l_shoulder_ys.append(y)
				l_shoulder_zs.append(z)
			if 'l_shoulder' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				r_shoulder_xs.append(x)
				r_shoulder_ys.append(y)
				r_shoulder_zs.append(z)
			if 'r_elbow' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				l_elbow_xs.append(x)
				l_elbow_ys.append(y)
				l_elbow_zs.append(z)
			if 'l_elbow' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				r_elbow_xs.append(x)
				r_elbow_ys.append(y)
				r_elbow_zs.append(z)
			if 'r_hand' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				l_hand_xs.append(x)
				l_hand_ys.append(y)
				l_hand_zs.append(z)
			if 'l_hand' in line:
				elems = line.split(' ')
				x = float(elems[2])
				y = float(elems[4])
				z = float(elems[6])
				r_hand_xs.append(x)
				r_hand_ys.append(y)
				r_hand_zs.append(z)

	gauss_head_xs = gaussian_filter1d(head_xs, sigma = 7)
	gauss_head_ys = gaussian_filter1d(head_ys, sigma = 7)
	gauss_head_zs = gaussian_filter1d(head_zs, sigma = 7)
	# l_shoulder_xs = gaussian_filter1d(l_shoulder_xs, sigma = 7)
	# l_shoulder_ys = gaussian_filter1d(l_shoulder_ys, sigma = 7)
	# l_shoulder_zs = gaussian_filter1d(l_shoulder_zs, sigma = 7)
	# r_shoulder_xs = gaussian_filter1d(r_shoulder_xs, sigma = 7)
	# r_shoulder_ys = gaussian_filter1d(r_shoulder_ys, sigma = 7)
	# r_shoulder_zs = gaussian_filter1d(r_shoulder_zs, sigma = 7)
	gauss_l_elbow_xs = gaussian_filter1d(l_elbow_xs, sigma = 7)
	gauss_l_elbow_ys = gaussian_filter1d(l_elbow_ys, sigma = 7)
	gauss_l_elbow_zs = gaussian_filter1d(l_elbow_zs, sigma = 7)
	# r_elbow_xs = gaussian_filter1d(r_elbow_xs, sigma = 7)
	# r_elbow_ys = gaussian_filter1d(r_elbow_ys, sigma = 7)
	# r_elbow_zs = gaussian_filter1d(r_elbow_zs, sigma = 7)
	gauss_l_hand_xs = gaussian_filter1d(l_hand_xs, sigma = 7)
	gauss_l_hand_ys = gaussian_filter1d(l_hand_ys, sigma = 7)
	gauss_l_hand_zs = gaussian_filter1d(l_hand_zs, sigma = 7)
	# r_hand_xs = gaussian_filter1d(r_hand_xs, sigma = 7)
	# r_hand_ys = gaussian_filter1d(r_hand_ys, sigma = 7)
	# r_hand_zs = gaussian_filter1d(r_hand_zs, sigma = 7)
	return gauss_l_elbow_xs, gauss_l_elbow_ys, gauss_l_elbow_zs, gauss_l_hand_xs, gauss_l_hand_ys, gauss_l_hand_zs, head_xs, head_ys, head_zs, gauss_head_xs, gauss_head_ys, gauss_head_zs, l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, r_hand_xs, r_hand_ys, r_hand_zs

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

def link_length(top_x, top_y, top_z, bot_x, bot_y, bot_z):
	return np.sqrt((bot_x - top_x) * (bot_x - top_x) + (bot_y - top_y) * (bot_y - top_y) + (bot_z - top_z) * (bot_z - top_z))

def main():
	gauss_l_elbow_xs, gauss_l_elbow_ys, gauss_l_elbow_zs, gauss_l_hand_xs, gauss_l_hand_ys, gauss_l_hand_zs, head_xs, head_ys, head_zs, gauss_head_xs, gauss_head_ys, gauss_head_zs, l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, r_hand_xs, r_hand_ys, r_hand_zs = process_input()


	l_elbow_xs = l_elbow_xs[400:]
	l_elbow_ys = l_elbow_ys[400:]
	l_elbow_zs = l_elbow_zs[400:]

	l_hand_xs = l_hand_xs[400:]
	l_hand_ys = l_hand_ys[400:]
	l_hand_zs = l_hand_zs[400:]

	gauss_l_elbow_xs = gauss_l_elbow_xs[400:]
	gauss_l_elbow_ys = gauss_l_elbow_ys[400:]
	gauss_l_elbow_zs = gauss_l_elbow_zs[400:]

	gauss_l_hand_xs = gauss_l_hand_xs[400:]
	gauss_l_hand_ys = gauss_l_hand_ys[400:]
	gauss_l_hand_zs = gauss_l_hand_zs[400:]



	diff_head = []
	elb_hand_links= []
	gauss_elb_hand_links =[]
	kalm_links = []
	gauss_links = []
	dif_gauss_links = []
	dif_kalm_links = []
	dif_elb_hand = []
	gauss_diff_head = []
	kalm_diff_head = []

	elb_xs = np.asarray(l_elbow_xs)
	elb_ys = np.asarray(l_elbow_ys)
	elb_zs = np.asarray(l_elbow_zs)

	hand_xs = np.asarray(l_hand_xs)
	hand_ys = np.asarray(l_hand_ys)
	hand_zs = np.asarray(l_hand_zs)

	elb_x_velocity, elb_y_velocity, elb_z_velocity = claculate_point_and_velocity(elb_xs, elb_ys, elb_zs)

	hand_x_velocity, hand_y_velocity, hand_z_velocity = claculate_point_and_velocity(hand_xs, hand_ys, hand_zs)

	sm_elb_x = np.squeeze(np.asarray(apply_kalman(elb_x_velocity)))
	sm_elb_y = np.squeeze(np.asarray(apply_kalman(elb_y_velocity)))
	sm_elb_z = np.squeeze(np.asarray(apply_kalman(elb_z_velocity)))

	sm_hand_x = np.squeeze(np.asarray(apply_kalman(hand_x_velocity)))
	sm_hand_y = np.squeeze(np.asarray(apply_kalman(hand_y_velocity)))
	sm_hand_z = np.squeeze(np.asarray(apply_kalman(hand_z_velocity)))

	for i in range(0, len(l_elbow_xs)-2):
		diff_head.append(link_length(head_xs[i], head_ys[i], head_zs[i], head_xs[i+1], head_ys[i+1], head_zs[i+1]))
		gauss_diff_head.append(link_length(gauss_head_xs[i], gauss_head_ys[i], gauss_head_zs[i], gauss_head_xs[i+1], gauss_head_ys[i+1], gauss_head_zs[i+1]))
		elb_hand_links.append(link_length(l_elbow_xs[i], l_elbow_ys[i], l_elbow_zs[i], l_hand_xs[i], l_hand_ys[i], l_hand_zs[i]))
		gauss_links.append(link_length(gauss_l_elbow_xs[i], gauss_l_elbow_ys[i], gauss_l_elbow_zs[i], gauss_l_hand_xs[i], gauss_l_hand_ys[i], gauss_l_hand_zs[i]))


	for i in range(0, len(elb_hand_links)-1):
		dif_elb_hand.append(elb_hand_links[i] - elb_hand_links[i+1])
		dif_gauss_links.append(gauss_links[i] - gauss_links[i+1])


	for i in range(0, len(sm_elb_x)-2):
		kalm_links.append(link_length(sm_elb_x[i], sm_elb_y[i], sm_elb_z[i], sm_hand_x[i], sm_hand_y[i], sm_hand_z[i]))
		#kalm_diff_head.append(link_length(sm_x[i], sm_y[i], sm_z[i], sm_x[i+1], sm_y[i+2], sm_z[i+1]))

	for i in range(0, len(kalm_links)-1):
		dif_kalm_links.append(kalm_links[i]-kalm_links[i+1])


	pylab.ylabel('Link Length Difference')
	pylab.xlabel('Frame number')
	pylab.plot(dif_elb_hand[10:], label = 'Raw data')
	pylab.plot(dif_gauss_links[10:], label = 'Gaussian Filter')
	pylab.plot(dif_kalm_links[10:], label = 'Kalman Filter')
	pylab.legend(loc='upper left')
	pylab.savefig("figs/filters.pdf")
	pylab.show()


	print(np.mean(dif_elb_hand))
	print(np.std(dif_elb_hand))


if __name__ == "__main__":
    main() 


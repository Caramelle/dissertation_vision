import numpy as np
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

	with open("rami_tracking_data.txt") as infile:
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

	# l_shoulder_xs = gaussian_filter1d(l_shoulder_xs, sigma = 7)
	# l_shoulder_ys = gaussian_filter1d(l_shoulder_ys, sigma = 7)
	# l_shoulder_zs = gaussian_filter1d(l_shoulder_zs, sigma = 7)
	# r_shoulder_xs = gaussian_filter1d(r_shoulder_xs, sigma = 7)
	# r_shoulder_ys = gaussian_filter1d(r_shoulder_ys, sigma = 7)
	# r_shoulder_zs = gaussian_filter1d(r_shoulder_zs, sigma = 7)
	# l_elbow_xs = gaussian_filter1d(l_elbow_xs, sigma = 7)
	# l_elbow_ys = gaussian_filter1d(l_elbow_ys, sigma = 7)
	# l_elbow_zs = gaussian_filter1d(l_elbow_zs, sigma = 7)
	# r_elbow_xs = gaussian_filter1d(r_elbow_xs, sigma = 7)
	# r_elbow_ys = gaussian_filter1d(r_elbow_ys, sigma = 7)
	# r_elbow_zs = gaussian_filter1d(r_elbow_zs, sigma = 7)
	# l_hand_xs = gaussian_filter1d(l_hand_xs, sigma = 7)
	# l_hand_ys = gaussian_filter1d(l_hand_ys, sigma = 7)
	# l_hand_zs = gaussian_filter1d(l_hand_zs, sigma = 7)
	# r_hand_xs = gaussian_filter1d(r_hand_xs, sigma = 7)
	# r_hand_ys = gaussian_filter1d(r_hand_ys, sigma = 7)
	# r_hand_zs = gaussian_filter1d(r_hand_zs, sigma = 7)
	return l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, r_hand_xs, r_hand_ys, r_hand_zs

def determine_cadran(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z):
	if new_moving_y > origin_y and new_moving_x > origin_x:
		return 1
	if new_moving_y > origin_y and new_moving_x < origin_x:
		return 2
	if new_moving_y < origin_y and new_moving_x < origin_x:
		return 3
	if new_moving_y < origin_y and new_moving_x > origin_x:
		return 4

def cadran_angle(angle, cadran):
	if cadran == 1:
		return angle
	if cadran == 2:
		return np.pi - angle
	if cadran == 3:
		return np.pi + angle
	if cadran == 4:
		return -angle


def calculate_pitch(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z):
	#pitch = np.arctan((initial_moving_x - origin_x)/(initial_moving_z - origin_z)) - np.arctan((new_moving_x - origin_x)/(new_moving_z - origin_z))
	try:
		pitch = np.arctan((initial_moving_x - origin_x)/(initial_moving_z - origin_z))
	except:
		pitch = 0

	cadran = determine_cadran(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z)


	return cadran_angle(pitch, cadran)

def calculate_yaw(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z):	
	#yaw = np.arctan((initial_moving_y - origin_y)/(initial_moving_x - origin_x)) - np.arctan((new_moving_y - origin_y)/(new_moving_x - origin_x))
	try:
		yaw = np.arctan((initial_moving_y - origin_y)/(initial_moving_x - origin_x))
	except:
		yaw = 0

	cadran = determine_cadran(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z)

	return cadran_angle(yaw, cadran)

def calculate_roll(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z):
	#roll = np.arctan((initial_moving_z - origin_z)/(initial_moving_y - origin_y)) - np.arctan((new_moving_z - origin_z)/(new_moving_y - origin_y))
	roll = np.arctan((initial_moving_z - origin_z)/(initial_moving_y - origin_y))

	cadran = determine_cadran(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z)

	return cadran_angle(roll, cadran)

def calculate_angles(x, y, z, moving_xs, moving_ys, moving_zs):
	pitch = []
	roll = []
	yaw = []
	initial_x = moving_xs[0]
	initial_y = moving_ys[0]
	initial_z = moving_zs[0]

	for i in range(1, len(moving_xs)-1):
		pitch.append(calculate_pitch(x,y,z, initial_x, initial_y, initial_z, moving_xs[i], moving_ys[i], moving_zs[i]))
		roll.append(calculate_roll(x,y,z, initial_x, initial_y, initial_z, moving_xs[i], moving_ys[i], moving_zs[i]))
		yaw.append(calculate_yaw(x,y,z, initial_x, initial_y, initial_z, moving_xs[i], moving_ys[i], moving_zs[i]))
		initial_x = moving_xs[i]
		initial_y = moving_ys[i]
		initial_z = moving_zs[i]

	return pitch, roll, yaw

def calculate_trajectories(side, shoulder_pitch, shoulder_roll, shoulder_yaw, elbow_pitch, elbow_yaw):
	if side == 'l':
		with open('gauss_rami_tracefile_l.txt', 'w') as outfile:
			ZERO_VECTOR = "l 0.0 -1.0 2.0 1.0 0.0 0.0 0.0\n" 
			outfile.writelines(ZERO_VECTOR)
			for i in range(0, len(shoulder_pitch)):
				line = side + ' ' + str(shoulder_pitch[i]) + ' ' + str(shoulder_roll[i]) + ' ' + str(shoulder_yaw[i]) + ' ' + str(elbow_pitch[i]) + ' ' + str(elbow_yaw[i]) + ' 0.0 0.0 \n'
				#line = side + ' ' + '0.0' + ' ' + '0.0' + ' ' + '0.0' + ' ' + str(elbow_pitch[i]) + ' ' + str(elbow_yaw[i]) + ' 0.0 0.0 \n'				
				# elems = line.split(' ')
				# for i in range(1, (len(elems)-3)):
				# 	traj = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				# 	if elems[i] != '0.0':
				# 		traj[i-1] = elems[i]
				# 		traj_line = ' '.join(str(e) for e in traj)
				# 		traj_line = 'l '+ traj_line + '\n'
				outfile.writelines(line)
	if side == 'r':
		with open('gauss_rami_tracefile_r.txt', 'w') as outfile:
			for i in range(0, len(shoulder_pitch)):
				line = side + ' ' + str(shoulder_pitch[i]) + ' ' + str(shoulder_roll[i]) + ' ' + str(shoulder_yaw[i]) + ' ' + str(elbow_pitch[i]) + ' ' + str(elbow_yaw[i]) + ' 0.0 0.0 \n'
				outfile.writelines(line)


def main():
	l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, r_hand_xs, r_hand_ys, r_hand_zs = process_input()

	l_shoulder_pitch, l_shoulder_roll, l_shoulder_yaw = calculate_angles(l_shoulder_xs[0], l_shoulder_ys[0], l_shoulder_zs[0], l_elbow_xs, l_elbow_ys, l_elbow_zs)
	r_shoulder_pitch, r_shoulder_roll, r_shoulder_yaw = calculate_angles(r_shoulder_xs[0], r_shoulder_ys[0], r_shoulder_zs[0], r_elbow_xs, r_elbow_ys, r_elbow_zs)

	l_elbow_pitch, l_elbow_roll, l_elbow_yaw = calculate_angles(l_elbow_xs[0], l_elbow_ys[0], l_elbow_zs[0], l_hand_xs, l_hand_ys, l_hand_zs)
	r_elbow_pitch, r_elbow_roll, r_elbow_yaw = calculate_angles(r_elbow_xs[0], r_elbow_ys[0], r_elbow_zs[0], r_hand_xs, r_hand_ys, r_hand_zs)


	calculate_trajectories('l', l_shoulder_pitch, l_shoulder_roll, l_shoulder_yaw, l_elbow_pitch, l_elbow_yaw)
	calculate_trajectories('r', r_shoulder_pitch, r_shoulder_roll, r_shoulder_yaw, r_elbow_pitch, r_elbow_yaw)




if __name__ == "__main__":
    main() 


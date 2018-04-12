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

	with open("andreea_wave_swap_rotated.txt") as infile:
		for line in infile:
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

	l_shoulder_xs = gaussian_filter1d(l_shoulder_xs, sigma = 7)
	l_shoulder_ys = gaussian_filter1d(l_shoulder_ys, sigma = 7)
	l_shoulder_zs = gaussian_filter1d(l_shoulder_zs, sigma = 7)
	r_shoulder_xs = gaussian_filter1d(r_shoulder_xs, sigma = 7)
	r_shoulder_ys = gaussian_filter1d(r_shoulder_ys, sigma = 7)
	r_shoulder_zs = gaussian_filter1d(r_shoulder_zs, sigma = 7)
	l_elbow_xs = gaussian_filter1d(l_elbow_xs, sigma = 7)
	l_elbow_ys = gaussian_filter1d(l_elbow_ys, sigma = 7)
	l_elbow_zs = gaussian_filter1d(l_elbow_zs, sigma = 7)
	r_elbow_xs = gaussian_filter1d(r_elbow_xs, sigma = 7)
	r_elbow_ys = gaussian_filter1d(r_elbow_ys, sigma = 7)
	r_elbow_zs = gaussian_filter1d(r_elbow_zs, sigma = 7)
	l_hand_xs = gaussian_filter1d(l_hand_xs, sigma = 7)
	l_hand_ys = gaussian_filter1d(l_hand_ys, sigma = 7)
	l_hand_zs = gaussian_filter1d(l_hand_zs, sigma = 7)
	r_hand_xs = gaussian_filter1d(r_hand_xs, sigma = 7)
	r_hand_ys = gaussian_filter1d(r_hand_ys, sigma = 7)
	r_hand_zs = gaussian_filter1d(r_hand_zs, sigma = 7)
	return l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, r_hand_xs, r_hand_ys, r_hand_zs

def determine_cadran(top_1, top_2, bot_1, bot_2, side):
	if bot_2 > top_2 and bot_1 > top_1:
		return 1
	if bot_2 > top_2 and bot_1 < top_1:
		return 2
	if bot_2 < top_2 and bot_1 < top_1:
		return 3
	if bot_2 < top_2 and bot_1 > top_1:
		return 4


def cadran_angle(side, angle, cadran):
	if cadran == 1:
		if side == 'l':
			return angle
		if side == 'r':
			return np.pi - angle
	if cadran == 2:
		if side == 'l':
			return np.pi + angle
		if side == 'r':
			return -angle
	if cadran == 3:
		if side == 'l':
			return -np.pi + angle
		if side == 'r':
			return -angle
	if cadran == 4:
		if side == 'l':
			return angle
		if side =='r':
			return -np.pi - angle
	return angle


def calculate_pitch(top_x, top_z, bot_x, bot_z, side):
	#pitch = np.arctan((initial_moving_x - origin_x)/(initial_moving_z - origin_z)) - np.arctan((new_moving_x - origin_x)/(new_moving_z - origin_z))
	try:
		if bot_z - top_z == 0:
			bot_z = top_z + 0.001
		pitch = np.arctan((bot_x - top_x)/(bot_z - top_z))
	except:
		pitch = 0
	cadran = determine_cadran(top_x, top_z, bot_x, bot_z, side)
	#return pitch
	return cadran_angle(side, pitch, cadran)

def calculate_yaw(top_y, top_x, bot_y, bot_x, side):	
	#yaw = np.arctan((initial_moving_y - origin_y)/(initial_moving_x - origin_x)) - np.arctan((new_moving_y - origin_y)/(new_moving_x - origin_x))
	try:
		if bot_x - top_x == 0:
			bot_x = top_x + 0.001
		yaw = np.arctan((bot_y - top_y)/(bot_x - top_x))
	except:
		yaw = 0

	cadran = determine_cadran(top_y, top_x, bot_y, bot_x, side)
	#return yaw
	return cadran_angle(side, yaw, cadran)

def calculate_roll(top_z, top_y, bot_y, bot_z, side):
	#roll = np.arctan((initial_moving_z - origin_z)/(initial_moving_y - origin_y)) - np.arctan((new_moving_z - origin_z)/(new_moving_y - origin_y))
	try:
		roll = np.arctan((bot_z - top_z)/(bot_y - top_y))
	except:
		roll = 0

	cadran = determine_cadran(top_z, top_y, bot_y, bot_z, side)
	#return roll
	return cadran_angle(side, roll, cadran)


# def calculate_pitch(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z):
# 	#pitch = np.arctan((initial_moving_x - origin_x)/(initial_moving_z - origin_z)) - np.arctan((new_moving_x - origin_x)/(new_moving_z - origin_z))
# 	try:
# 		pitch = np.arctan((initial_moving_x - origin_x)/(initial_moving_z - origin_z))
# 	except:
# 		pitch = 0

# 	cadran = determine_cadran(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z)


# 	return cadran_angle(pitch, cadran)

# def calculate_yaw(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z):	
# 	# #yaw = np.arctan((initial_moving_y - origin_y)/(initial_moving_x - origin_x)) - np.arctan((new_moving_y - origin_y)/(new_moving_x - origin_x))
# 	# try:
# 	# 	yaw = np.arctan((initial_moving_y - origin_y)/(initial_moving_x - origin_x))
# 	# except:
# 	# 	yaw = 0

# 	# cadran = determine_cadran(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z)

# 	# return cadran_angle(yaw, cadran)

# def calculate_roll(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z):
# 	#roll = np.arctan((initial_moving_z - origin_z)/(initial_moving_y - origin_y)) - np.arctan((new_moving_z - origin_z)/(new_moving_y - origin_y))
# 	roll = np.arctan((initial_moving_z - origin_z)/(initial_moving_y - origin_y))

# 	cadran = determine_cadran(origin_x, origin_y, origin_z, initial_moving_x, initial_moving_y, initial_moving_z, new_moving_x, new_moving_y, new_moving_z)

# 	return cadran_angle(roll, cadran)

def calculate_angles(side, top_xs, top_ys, top_zs, bot_xs, bot_ys, bot_zs):
	pitch = []
	roll = []
	yaw = []

	for i in range(1, len(top_xs)-1):
		pitch.append(calculate_pitch(top_xs[i], top_zs[i], bot_xs[i], bot_zs[i], side))
		roll.append(calculate_roll(top_zs[i], top_ys[i], bot_ys[i], bot_zs[i], side))
		yaw.append(calculate_yaw(top_ys[i], top_xs[i], bot_ys[i], bot_xs[i], side))

	return pitch, roll, yaw


def calculate_elbow_angles(side, top_xs, top_ys, top_zs, bot_xs, bot_ys, bot_zs, shoulder_pitches, shoulder_rolls, shoulder_yaws):
	pitch = []
	roll = []
	yaw = []

	for i in range(1, len(top_xs)-1):
		if side =='l':
			pitch.append(calculate_pitch(top_xs[i], top_zs[i], bot_xs[i], bot_zs[i], side))
		else:
			pitch.append(calculate_pitch(top_xs[i], top_zs[i], bot_xs[i], bot_zs[i], side))			
		roll.append(calculate_roll(top_zs[i], top_ys[i], bot_ys[i], bot_zs[i], side) - shoulder_rolls[i-1])
		yaw.append(calculate_yaw(top_ys[i], top_xs[i], bot_ys[i], bot_xs[i], side))

	return pitch, roll, yaw

def calculate_trajectories(side, shoulder_pitch, shoulder_roll, shoulder_yaw, elbow_pitch, elbow_yaw):
	if side == 'l':
		with open('wave_swap_tracefile_l_l.txt', 'w') as outfile:
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
		with open('wave_swap_tracefile_r.txt', 'w') as outfile:
			for i in range(0, len(shoulder_pitch)):
				line = side + ' ' + str(shoulder_pitch[i]) + ' ' + str(shoulder_roll[i]) + ' ' + str(shoulder_yaw[i]) + ' ' + str(elbow_pitch[i]) + ' ' + str(elbow_yaw[i]) + ' 0.0 0.0 \n'
				outfile.writelines(line)

# def getRotationMatrix(x, y, z):
# 	dx = np.sqrt(y * y + z * z)
# 	dy = np.sqrt(x * x + z * z)
# 	dz = np.sqrt(x * x + y * y)
# 	cx = double(y/dx)
# 	sx = double(z/dx)
# 	cy = double(z/dy)
# 	sy = double(x/dy)
# 	xz = double(x/dz)
# 	sz = double(y/dz)
# 	rot[0][0] = cy*cz
#     rot[0][1] = -cy*sz
#     rot[0][2] = sy
#     rot[1][0] = sx*sy*cz+cx*sz
#     rot[1][1] = -sx*sy*sz+cx*cz
#     rot[1][2] = -sx*cy
#     rot[2][0] = -cx*sy*cz+sx*sz
#     rot[2][1] = cx*sy*sz+sx*cz
#     rot[2][2] = cx*cy
#     return rot


def correct_elbows(elbow_x, elbow_y, elbow_z, shoulder_x, shoulder_y, shoulder_z):
	for i in range(0, len(elbow_x) -1):
		elbow_x[i] = elbow_x[i] - shoulder_x[i]
		elbow_y[i] = elbow_y[i] - shoulder_y[i]
		elbow_z[i] = elbow_z[i] - shoulder_z[i]
	return elbow_x, elbow_y, elbow_z


def main():
	l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, r_hand_xs, r_hand_ys, r_hand_zs = process_input()

	l_elbow_xs, l_elbow_ys, l_elbow_zs = correct_elbows(l_elbow_xs, l_elbow_ys, l_elbow_zs, l_shoulder_xs, l_shoulder_ys, l_shoulder_zs)
	l_hand_xs, l_hand_ys, l_hand_zs = correct_elbows(l_hand_xs, l_hand_ys, l_hand_zs, l_shoulder_xs, l_shoulder_ys, l_shoulder_zs)

	r_elbow_xs, r_elbow_ys, r_elbow_zs = correct_elbows(r_elbow_xs, r_elbow_ys, r_elbow_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs)
	r_hand_xs, r_hand_ys, r_hand_zs = correct_elbows(r_hand_xs, r_hand_ys, r_hand_zs, r_shoulder_xs, r_shoulder_ys, r_shoulder_zs)

	l_shoulder_pitch, l_shoulder_roll, l_shoulder_yaw = calculate_angles('l', l_shoulder_xs, l_shoulder_ys, l_shoulder_zs, l_elbow_xs, l_elbow_ys, l_elbow_zs)
	r_shoulder_pitch, r_shoulder_roll, r_shoulder_yaw = calculate_angles('r', r_shoulder_xs, r_shoulder_ys, r_shoulder_zs, r_elbow_xs, r_elbow_ys, r_elbow_zs)

	l_elbow_pitch, l_elbow_roll, l_elbow_yaw = calculate_elbow_angles('l', l_elbow_xs, l_elbow_ys, l_elbow_zs, l_hand_xs, l_hand_ys, l_hand_zs, l_shoulder_pitch, l_shoulder_roll, l_shoulder_yaw)
	r_elbow_pitch, r_elbow_roll, r_elbow_yaw = calculate_elbow_angles('r', r_elbow_xs, r_elbow_ys, r_elbow_zs, r_hand_xs, r_hand_ys, r_hand_zs, r_shoulder_pitch, r_shoulder_roll, r_shoulder_yaw)

	calculate_trajectories('l', l_shoulder_pitch, l_shoulder_roll, l_shoulder_yaw, l_elbow_pitch, l_elbow_yaw)
	calculate_trajectories('r', r_shoulder_pitch, r_shoulder_roll, r_shoulder_yaw, r_elbow_pitch, r_elbow_yaw)




if __name__ == "__main__":
    main() 


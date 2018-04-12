import numpy as np
from scipy.ndimage.filters import gaussian_filter1d


def get_angle(head_x, head_y, head_z, torso_x, torso_y, torso_z):
	print(head_y)
	head_x, head_y, head_z = rotate180(np.pi, head_x, head_y, head_z)
	print(head_y)
	torso_x, torso_y, torso_z = rotate180(np.pi, torso_x, torso_y, torso_z)
	angle = np.arctan((torso_x - head_x)/(torso_y - head_y))
	print(angle)
	return angle


def rotate180(angle, x, y, z):
	temp_x = x
	temp_y = y
	x = temp_x * (np.cos(angle)) - temp_y * (np.sin(angle))
	y = temp_x * (np.sin(angle)) + temp_y * (np.cos(angle)) 
	return x, y, z

def rotate(angle, x, y, z):
	temp_y = y
	temp_z = z
	y = temp_y * (np.cos(angle)) - temp_z * (np.sin(angle))
	z = temp_y * (np.sin(angle)) + temp_z * (np.cos(angle)) 
	return x, y, z

def get_fix_input():
	got_head = False
	got_torso = False
	with open("andreea_wave_clean.txt") as infile:
		for line in infile:
			if got_head == False or got_torso == False:
				if 'l_hip' in line and got_head == False:
					elems = line.split(' ')
					head_y = float(elems[2])
					head_x = float(elems[4])
					head_z = float(elems[6])
					got_head = True
				if 'l_foot' in line and got_torso == False:
					elems = line.split(' ')
					torso_y = float(elems[2])
					torso_x = float(elems[4])
					torso_z = float(elems[6])
					got_torso = True
			else:
				break
	angle = get_angle(head_x, head_y, head_z, torso_x, torso_y, torso_z)
	return angle

def correct_file(angle):
	with open("andreea_wave_clean.txt") as infile, open('andreea_wave_just_rot.txt', 'w') as outfile:
		for line in infile:
			if 'head' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'neck' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'l_shoulder' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'r_shoulder' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'l_elbow' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'r_elbow' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'l_hand' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'r_hand' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'torso' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'l_hip' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'r_hip' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'l_knee' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'r_knee' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'l_foot' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)
			if 'r_foot' in line:
				elems = line.split(' ')
				y = float(elems[2])
				x = float(elems[4])
				z = float(elems[6])
				rot_x, rot_y, rot_z = rotate180(np.pi, x, y, z)
				good_x, good_y, good_z = rotate(angle, rot_x, rot_y, rot_z)
				newline = str(elems[0]) + " " + str(elems[1]) + " " + str(good_x) + " " + str(elems[3])+ " " + str(good_y) + " " + str(elems[5]) + " " + str(good_z) + "\n"
				outfile.writelines(newline)

def main():
	print("hi")
	angle = get_fix_input()
	print(angle)
	correct_file(angle)

if __name__ == "__main__":
    main() 

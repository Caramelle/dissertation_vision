from functools import reduce
import numpy as np
import math

print("hi")
l_shoulder_pitch =[]
l_shoulder_roll = []
l_shoulder_yaw = []
l_elb_pitch = []
l_elb_yaw = []
r_shoulder_pitch =[]
r_shoulder_roll = []
r_shoulder_yaw = []
r_elb_pitch = []
r_elb_yaw = []
desired_l_shoulder_pitch =[]
desired_l_shoulder_roll = []
desired_l_shoulder_yaw = []
desired_l_elb_pitch = []
desired_l_elb_yaw = []
desired_r_shoulder_pitch =[]
desired_r_shoulder_roll = []
desired_r_shoulder_yaw = []
desired_r_elb_pitch = []
desired_r_elb_yaw = []
with open("grasp_achieved.txt") as inputfile:
	for line in inputfile:
		if 'position' in line:
			line = str(line)
			line = line.replace(':', '')
			line = line.replace('[', '')
			line = line.replace(']', '')
			line = line.replace('\'', '')
			line = line.replace(',','')
			elems = line.split(" ")
			l_shoulder_pitch.append(float(elems[16]))
			l_shoulder_roll.append(float(elems[17]))
			l_shoulder_yaw.append(float(elems[18]))
			l_elb_pitch.append(float(elems[19]))
			l_elb_yaw.append(float(elems[20]))
			r_shoulder_pitch.append(float(elems[27]))
			r_shoulder_roll.append(float(elems[28]))
			r_shoulder_yaw.append(float(elems[29]))
			r_elb_pitch .append(float(elems[30]))
			r_elb_yaw.append(float(elems[31]))

with open("grasp_swap_tracefile_l.txt") as inputfile:
	for line in inputfile:
		line = str(line)
		elems = line.split(" ")
		desired_l_shoulder_pitch.append(float(elems[1]))
		desired_l_shoulder_roll.append(float(elems[2]))
		desired_l_shoulder_yaw.append(float(elems[3]))
		desired_l_elb_pitch.append(float(elems[4]))
		desired_l_elb_yaw.append(float(elems[5]))

with open("grasp_swap_tracefile_r.txt") as inputfile:
	for line in inputfile:
		line = str(line)
		elems = line.split(" ")
		desired_r_shoulder_pitch.append(float(elems[1]))
		desired_r_shoulder_roll.append(float(elems[2]))
		desired_r_shoulder_yaw.append(float(elems[3]))
		desired_r_elb_pitch .append(float(elems[4]))
		desired_r_elb_yaw.append(float(elems[5]))



offset = 1200
num = 3
print(len(l_shoulder_pitch))
# print(l_shoulder_pitch)
print(len(desired_l_shoulder_pitch))
# print(desired_l_shoulder_pitch)
l_shoulder_pitch = l_shoulder_pitch[offset::num]
l_shoulder_roll = l_shoulder_roll[offset::num]
l_shoulder_yaw = l_shoulder_yaw[offset::num]
l_elb_pitch = l_elb_pitch[offset::num]
l_elb_yaw = l_elb_yaw[offset::num]
r_shoulder_pitch = r_shoulder_pitch[offset::num]
r_shoulder_roll = r_shoulder_roll[offset::num]
r_shoulder_yaw = r_shoulder_yaw[offset::num]
r_elb_pitch = r_elb_pitch[offset::num]
r_elb_yaw = r_elb_yaw[offset::num]
print(len(desired_l_shoulder_pitch))
print(len(l_shoulder_pitch))
print((l_shoulder_pitch))
print("ugh")
print(desired_l_shoulder_pitch)

dif_l_shoulder_pitch =[]
dif_l_shoulder_roll = []
dif_l_shoulder_yaw = []
dif_l_elb_pitch = []
dif_l_elb_yaw = []
dif_r_shoulder_pitch =[]
dif_r_shoulder_roll = []
dif_r_shoulder_yaw = []
dif_r_elb_pitch = []
dif_r_elb_yaw = []
print(len(desired_l_shoulder_pitch))
print("hi")
print(len(l_shoulder_pitch))

for i in range(0, len(l_shoulder_pitch)-1):
	dif_l_shoulder_pitch.append(abs(abs(l_shoulder_pitch[i]) - abs(desired_l_shoulder_pitch[i])))
	dif_l_shoulder_roll.append(abs(abs(l_shoulder_roll[i]) - abs(desired_l_shoulder_roll[i])))
	dif_l_shoulder_yaw.append(abs(abs(l_shoulder_yaw[i]) - abs(desired_l_shoulder_yaw[i])))
	dif_l_elb_pitch.append(abs(abs(l_elb_pitch[i]) - abs(desired_l_elb_pitch[i])))
	dif_l_elb_yaw.append(abs(abs(l_elb_yaw[i]) - abs(desired_l_elb_yaw[i])))
	dif_r_shoulder_pitch.append(abs(abs(r_shoulder_pitch[i]) - abs(desired_r_shoulder_pitch[i])))
	dif_r_shoulder_roll.append(abs(abs(r_shoulder_roll[i]) - abs(desired_r_shoulder_roll[i])))
	dif_r_shoulder_yaw.append(abs(abs(r_shoulder_yaw[i]) - abs(desired_r_shoulder_yaw[i])))
	dif_r_elb_pitch .append(abs(abs(r_elb_pitch[i]) - abs(desired_r_elb_pitch[i])))
	dif_r_elb_yaw.append(abs(abs(r_elb_yaw[i]) - abs(desired_r_elb_yaw[i])))


# print(r_elb_pitch)
# print(desired_r_elb_pitch)

print("std dev")
print("l sh pitch", np.std(dif_l_shoulder_pitch))

print("l sh roll", np.std(dif_l_shoulder_roll))

print("l sh yaw", np.std(dif_l_shoulder_yaw))

print("l elb pitch", np.std(dif_l_elb_pitch))

print("l elb yaw", np.std(dif_l_elb_yaw))



print("r sh pitch", np.std(dif_r_shoulder_pitch))

print("r sh roll", np.std(dif_r_shoulder_roll))

print("r sh yaw", np.std(dif_r_shoulder_yaw))

print("r elb pitch", np.std(dif_r_elb_pitch))

print("r elb yaw", np.std(dif_r_elb_yaw))


print("mean")
print("l sh pitch", np.mean(dif_l_shoulder_pitch))

print("l sh roll", np.mean(dif_l_shoulder_roll))

print("l sh yaw", np.mean(dif_l_shoulder_yaw))

print("l elb pitch", np.mean(dif_l_elb_pitch))

print("l elb yaw", np.mean(dif_l_elb_yaw))



print("r sh pitch", np.mean(dif_r_shoulder_pitch))

print("r sh roll", np.mean(dif_r_shoulder_roll))

print("r sh yaw", np.mean(dif_r_shoulder_yaw))

print("r elb pitch", np.mean(dif_r_elb_pitch))

print("r elb yaw", np.mean(dif_r_elb_yaw))

print(dif_l_shoulder_roll)
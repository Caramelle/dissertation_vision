import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


path = 'plot.txt'

file = open(path, 'r')

xs = []
ys = []
zs = []

count = 0
for line in file:
		if len(line) > 5:
			elems = line.split(' ')
			xs.append(float(elems[2]))
			ys.append(float(elems[4]))
			zs.append(float(elems[6]))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



"""
make left & right hip be in the same plane
"""
# for i in range (0, 15):
# 	temp_y = ys[i]
# 	temp_z = zs[i]
# 	alpha = 50.
# 	ys[i] = temp_y * (np.cos(np.pi/4.)) - temp_z * (np.sin(np.pi/4.))
# 	zs[i] = temp_y * (np.sin(np.pi/4.)) + temp_z * (np.cos(np.pi/4.)) 

# for i in range (0, 15):
# 	temp_y = ys[i]
# 	temp_z = zs[i]
# 	alpha = 40.
# 	ys[i] = temp_y * (np.cos(alpha * np.pi /180.)) - temp_z * (np.sin(alpha * np.pi /180.))
# 	zs[i] = temp_y * (np.sin(alpha * np.pi /180.)) + temp_z * (np.cos(alpha * np.pi /180.)) 

# for i in range (0, 15):
# 	temp_x = xs[i]
# 	xs[i] = -0.8 * temp_x


head_neck_x = [xs[0], xs[1]]
head_neck_y = [ys[0], ys[1]]
head_neck_z = [zs[0], zs[1]]

neck_l_shoulder_x = [xs[1], xs[2]]
neck_l_shoulder_y = [ys[1], ys[2]]
neck_l_shoulder_z = [zs[1], zs[2]]

neck_r_shoulder_x = [xs[2], xs[3]]
neck_r_shoulder_y = [ys[2], ys[3]]
neck_r_shoulder_z = [zs[2], zs[3]]

l_shoulder_elbow_x = [xs[2], xs[4]]
l_shoulder_elbow_y = [ys[2], ys[4]]
l_shoulder_elbow_z = [zs[2], zs[4]]

r_shoulder_elbow_x = [xs[3], xs[5]]
r_shoulder_elbow_y = [ys[3], ys[5]]
r_shoulder_elbow_z = [zs[3], zs[5]]

l_elbow_hand_x = [xs[4], xs[6]]
l_elbow_hand_y = [ys[4], ys[6]]
l_elbow_hand_z = [zs[4], zs[6]]

r_elbow_hand_x = [xs[5], xs[7]]
r_elbow_hand_y = [ys[5], ys[7]]
r_elbow_hand_z = [zs[5], zs[7]]

l_shoulder_torso_x = [xs[2], xs[8]]
l_shoulder_torso_y = [ys[2], ys[8]]
l_shoulder_torso_z = [zs[2], zs[8]]

r_shoulder_torso_x = [xs[3], xs[8]]
r_shoulder_torso_y = [ys[3], ys[8]]
r_shoulder_torso_z = [zs[3], zs[8]]

torso_l_hip_x = [xs[8], xs[9]]
torso_l_hip_y = [ys[8], ys[9]]
torso_l_hip_z = [zs[8], zs[9]]

torso_r_hip_x = [xs[8], xs[10]]
torso_r_hip_y = [ys[8], ys[10]]
torso_r_hip_z = [zs[8], zs[10]]

l_hip_knee_x = [xs[9], xs[11]]
l_hip_knee_y = [ys[9], ys[11]]
l_hip_knee_z = [zs[9], zs[11]]

r_hip_knee_x = [xs[10], xs[12]]
r_hip_knee_y = [ys[10], ys[12]]
r_hip_knee_z = [zs[10], zs[12]]

l_knee_foot_x = [xs[11], xs[13]]
l_knee_foot_y = [ys[11], ys[13]]
l_knee_foot_z = [zs[11], zs[13]]

r_knee_foot_x = [xs[12], xs[14]]
r_knee_foot_y = [ys[12], ys[14]]
r_knee_foot_z = [zs[12], zs[14]]

hips_x = [xs[9], xs[10]]
hips_y = [ys[9], ys[10]]
hips_z = [zs[9], zs[10]]


ax.plot(head_neck_x, head_neck_y, head_neck_z)
ax.plot(neck_l_shoulder_x, neck_l_shoulder_y, neck_l_shoulder_z)
ax.plot(neck_r_shoulder_x, neck_r_shoulder_y, neck_r_shoulder_z)
ax.plot(l_elbow_hand_x, l_elbow_hand_y, l_elbow_hand_z)
ax.plot(r_elbow_hand_x, r_elbow_hand_y, r_elbow_hand_z)
ax.plot(l_shoulder_torso_x, l_shoulder_torso_y, l_shoulder_torso_z)
ax.plot(r_shoulder_torso_x, r_shoulder_torso_y, r_shoulder_torso_z)
ax.plot(torso_l_hip_x, torso_l_hip_y, torso_l_hip_z)
ax.plot(torso_r_hip_x, torso_r_hip_y, torso_r_hip_z)
ax.plot(l_hip_knee_x, l_hip_knee_y, l_hip_knee_z)
ax.plot(r_hip_knee_x, r_hip_knee_y, r_hip_knee_z)
ax.plot(l_knee_foot_x, l_knee_foot_y, l_knee_foot_z)
ax.plot(r_knee_foot_x, r_knee_foot_y, r_knee_foot_z)
ax.plot(l_shoulder_elbow_x, l_shoulder_elbow_y, l_shoulder_elbow_z)
ax.plot(r_shoulder_elbow_x, r_shoulder_elbow_y, l_shoulder_elbow_z)
ax.plot(hips_x, hips_y, hips_z)




plt.show()
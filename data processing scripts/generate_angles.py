import numpy as np

shoulder_x = -482.614
shoulder_y = 527.554
shoulder_z = 2784.39
prev_elbow_x = -657.097
prev_elbow_y = 520.934
prev_elbow_z = 2842.75
new_elbow_x = -645.843
new_elbow_y = 518.993
new_elbow_z = 2824.8
prev_hand_x = -802.799
prev_hand_y = 558.387
prev_hand_z = 2704.59
new_hand_x = -768.335
new_hand_y = 544.135
new_hand_z = 2710


#rotation around z axis
shoulder_yaw = np.arctan((prev_elbow_y - shoulder_y)/(prev_elbow_x - shoulder_x)) - np.arctan((new_elbow_y - shoulder_y)/(new_elbow_x - shoulder_x))

#rotation around x axis
shoulder_roll = np.arctan((prev_elbow_z - shoulder_z)/(prev_elbow_y - shoulder_y)) - np.arctan((new_elbow_z - shoulder_z)/(new_elbow_y - shoulder_y))

#rotation around y axis
shoulder_pitch = np.arctan((prev_elbow_x - shoulder_x)/(prev_elbow_z - shoulder_z)) - np.arctan((new_elbow_x - shoulder_x)/(new_elbow_z - shoulder_z))



elbow_yaw = np.arctan((prev_hand_y - prev_elbow_y)/(prev_hand_x - prev_elbow_x)) - np.arctan((new_hand_y - prev_elbow_y)/(new_hand_x - prev_elbow_x))

#rotation around x axis
elbow_roll = np.arctan((prev_hand_z - prev_elbow_z)/(prev_hand_y - prev_elbow_y)) - np.arctan((new_hand_z - prev_elbow_z)/(new_hand_y - prev_elbow_y))

#rotation around y axis
elbow_pitch = np.arctan((prev_hand_x - prev_elbow_x)/(prev_hand_z - prev_elbow_z)) - np.arctan((new_hand_x - prev_elbow_x)/(new_hand_z - prev_elbow_z))


print(shoulder_pitch, shoulder_roll, shoulder_yaw)
print(elbow_pitch, elbow_roll, elbow_yaw)
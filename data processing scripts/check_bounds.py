with open("grasp_swap_tracefile_r.txt") as infile:
	changed = 0
	not_changed = 0
	for line in infile:
		traj = line.split(' ')
		if float(traj[5]) < -2.019:
			changed = changed + 1
		else:
			if float(traj[5]) >  3.14:
				changed = changed + 1
			else:
				not_changed = not_changed + 1

print(changed, not_changed)

 #         """
    #         right elbow pitch issues
    #         """
    #         if traj[3] < -0.12:
    #             traj[3] = -0.12
    #         if traj[3] > 2.174:
    #             traj[3] = 2.174

    #         """
    #         right shoulder roll issues
    #         """
    #         if traj[1] < -1.226:
    #             traj[1] = -1.226
    #         if traj[1] > 1.519:
    #             traj[1] = 1.519

    #         """
    #         right shoudler yaw issues:
    #         """
    #         if traj[2] < -3.1:
    #             traj[2] = -3.1
    #         if traj[2] > 2.18:
    #             traj[2] = 2.18

            
    #         """
    #         right forearm yaw issues
    #         """
    #         if traj[4] < -2.019:
    #             traj[4] = -2.019
    #         if traj[4] > 3.14:
    #             traj[4] = 3.14

    #         """
    #         right sh pitch issues
    #         """
    #         if traj[0] < -2.85:
    #             traj[0] = -2.85
    #         if traj[0] > 2.0:
    #             traj[0] = 2.0



            # """
            # left elbow pitch issues
            # """
            # if traj[3] < -2.174:
            #     traj[3] = -2.174
            # if traj[3] > 0.12:
            #     traj[3] = 0.12

            # """
            # left shoulder roll issues
            # """
            # if traj[1] < -1.519:
            #     traj[1] = -1.519
            # if traj[1] > 1.266:
            #     traj[1]= 1.266

            # """
            # left shoudler yaw issues:
            # """
            # if traj[2] < -3.1:
            #     traj[2] = -3.1
            # if traj[2] > 2.18:
            #     traj[2] = 2.18

            # """
            # left shoudler pitch issues:
            # """

            # if traj[0] < -2.85:
            #     traj[0] = -2.85
            # if traj[0] > 2.0:
            #     traj[0] = 2.0

            # """
            # left forearm yaw issues
            # """
            # if traj[4] < -2.019:
            #     traj[4] = -2.019
            # if traj[4] > 3.14:
            #     traj[4] = 3.14

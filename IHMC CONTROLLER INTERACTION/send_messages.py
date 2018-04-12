#!/usr/bin/env python

import copy
import time
import rospy
import roslib
from numpy import append

from ihmc_msgs.msg import ArmTrajectoryRosMessage
from ihmc_msgs.msg import OneDoFJointTrajectoryRosMessage
from ihmc_msgs.msg import TrajectoryPoint1DRosMessage
from sensor_msgs.msg import JointState as JointStatePR2


def sendRightArmTrajectory():
    
    with open("tracefile_l.txt") as infile:
        msg = ArmTrajectoryRosMessage()

        msg.robot_side = ArmTrajectoryRosMessage.LEFT
        msg.unique_id = -1
        msg.execution_mode = 0
        for line in infile:
            time = 2.0
            # if i == 1:
                
            #     #msg = appendTrajectoryPoint(msg, time, [0.0, -1.0, 2.0, 1.0, 0.0, 0.0, 0.0])

            #     time = time + 1.0
            # else:
            #     msg = ArmTrajectoryRosMessage()

            #     msg.robot_side = ArmTrajectoryRosMessage.LEFT
            #     msg.unique_id = -1
            #     msg.execution_mode = 0
            #     msg.previous_message_id = 0

            elems = line.split(' ')
            traj = []
            traj.append(float(elems[1]))
            traj.append(-float(elems[2]))
            traj.append(float(elems[3]))
            traj.append(float(elems[4]))
            traj.append(float(elems[5]))
            traj.append(float(elems[6]))
            traj.append(float(elems[7]))
            #print(traj)

            """
            left elbow pitch issues
            """
            if traj[3] < -2.174:
                traj[3] = -2.174
            if traj[3] > 0.12:
                traj[3] = 0.12

            """
            left shoulder roll issues
            """
            if traj[1] < -1.519:
                traj[1] = -1.519
            if traj[1] > 1.266:
                traj[1]= 1.266

            """
            left shoudler yaw issues:
            """
            if traj[2] < -3.1:
                traj[2] = -3.1
            if traj[2] > 2.18:
                traj[2] = 2.18

            """
            left shoudler pitch issues:
            """

            if traj[0] < -2.85:
                traj[0] = -2.85
            if traj[0] > 2.0:
                traj[0] = 2.0

            """
            left forearm yaw issues
            """
            if traj[4] < -2.019:
                traj[4] = -2.019
            if traj[4] > 3.14:
                traj[4] = 3.14

            msg = appendTrajectoryPoint(msg, time, traj)
            time = time + 500.0
        attempts = 0
        while attempts < 5:
            try:
                armTrajectoryPublisher.publish(msg)
                time.sleep(1)
                print('publised left message')
                i = i + 1
                attempts = 6
            except:
                print("msg left failed, ignoring")
                attempts = attempts + 1

    with open("tracefile_r.txt") as infile:
        msg = ArmTrajectoryRosMessage()

        msg.robot_side = ArmTrajectoryRosMessage.RIGHT
        msg.unique_id = -1
        msg.execution_mode = 0
        for line in infile:
            time = 2.0
            # if i == 1:
                
            #     #msg = appendTrajectoryPoint(msg, time, [0.0, -1.0, 2.0, 1.0, 0.0, 0.0, 0.0])

            #     time = time + 1.0
            # else:
            #     msg = ArmTrajectoryRosMessage()

            #     msg.robot_side = ArmTrajectoryRosMessage.LEFT
            #     msg.unique_id = -1
            #     msg.execution_mode = 0
            #     msg.previous_message_id = 0

            elems = line.split(' ')
            traj = []
            traj.append(float(elems[1]))
            traj.append(float(elems[2]))
            traj.append(float(elems[3]))
            traj.append(float(elems[4]))
            traj.append(float(elems[5]))
            traj.append(float(elems[6]))
            traj.append(float(elems[7]))
            #print(traj)

            """
            right elbow pitch issues
            """
            if traj[3] < -0.12:
                traj[3] = -0.12
            if traj[3] > 2.174:
                traj[3] = 2.174

            """
            right shoulder roll issues
            """
            if traj[1] < -1.226:
                traj[1] = -1.226
            if traj[1] > 1.519:
                traj[1] = 1.519

            """
            right shoudler yaw issues:
            """
            if traj[2] < -3.1:
                traj[2] = -3.1
            if traj[2] > 2.18:
                traj[2] = 2.18

            
            """
            right forearm yaw issues
            """
            if traj[4] < -2.019:
                traj[4] = -2.019
            if traj[4] > 3.14:
                traj[4] = 3.14

            """
            right sh pitch issues
            """
            if traj[0] < -2.85:
                traj[0] = -2.85
            if traj[0] > 2.0:
                traj[0] = 2.0

            msg = appendTrajectoryPoint(msg, time, traj)
            time = time + 500.0
        attempts = 0
        while attempts < 3:
            try:
                armTrajectoryPublisher.publish(msg)
                time.sleep(1)
                print('publised right message')
                i = i + 1
                attempts = 6
            except:
                print("msg right failed, ignoring")
                attempts = attempts + 1
            
    

def appendTrajectoryPoint(arm_trajectory, time, positions):
    if not arm_trajectory.joint_trajectory_messages:
        arm_trajectory.joint_trajectory_messages = [copy.deepcopy(OneDoFJointTrajectoryRosMessage()) for i in range(len(positions))]
    for i, pos in enumerate(positions):
        point = TrajectoryPoint1DRosMessage()
        point.time = time
        point.position = pos
        point.velocity = 0
        arm_trajectory.joint_trajectory_messages[i].trajectory_points.append(point)
    return arm_trajectory

if __name__ == '__main__':
    try:
        rospy.init_node('ihmc_arm_demo1')

        ROBOT_NAME = rospy.get_param('/ihmc_ros/robot_name')

        armTrajectoryPublisher = rospy.Publisher("/ihmc_ros/{0}/control/arm_trajectory".format(ROBOT_NAME), ArmTrajectoryRosMessage, queue_size=1)

        rate = rospy.Rate(10) # 10hz
        time.sleep(1)

        # make sure the simulation is running otherwise wait
        if armTrajectoryPublisher.get_num_connections() == 0:
            rospy.loginfo('waiting for subscriber...')
            while armTrajectoryPublisher.get_num_connections() == 0:
                rate.sleep()

        if not rospy.is_shutdown():
            sendRightArmTrajectory()
            #s = JointStatePublisher()
            time.sleep(5)

    except rospy.ROSInterruptException:
        pass
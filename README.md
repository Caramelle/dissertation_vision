Kinect data was captured using Simon Kaliski's implementation, as referenced in the report. 

All the code for processing the kinect data, including smoothing, rotating, cleaning, filering and joint angle generation is the the folder /data processing scripts. Note that all scripts expect the datafiles to be in the same folder. 
Most important script: process_trace.py -> uses a pose corrected trace file to generate joint angles and process them into a trajectory message

The script for sending IHMC messages to the robot is available in the IHMC CONTROLLER INTERACTION folder. 
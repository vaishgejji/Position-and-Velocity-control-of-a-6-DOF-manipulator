#!/usr/bin/env python3
import rospy
import math
import numpy as np 
from sensor_msgs.msg import JointState

def callback(data):
	q1 = data.position[0]
	q2 = data.position[1]
	q3 = data.position[2]
        
	J_det = [[-math.sin(q1+q2) - math.sin(q1), -math.sin(q1+q2), 0], [math.cos(q1+q2) + math.cos(q1), math.cos(q1+q2), 0], [0, 0, 1]]
	determinant = np.linalg.det(J_det)
	print("The determinant of the Jacobian matrix is: ")
	print(determinant)

rospy.init_node('determinant')
rospy.Subscriber("joint_states", JointState, callback)
rospy.spin()


#!/usr/bin/env python3
import rospy
import math
import numpy as np 
from sensor_msgs.msg import JointState
from control_msgs.msg import JointControllerState
from std_msgs.msg import Float64
from rrbot_control.srv import *

def c1(data):
	print(data.process_value)

def callback(data):
	q1 = data.position[0]
	q2 = data.position[1]
	q3 = data.position[2]
	
	# Call the service to find out the joint velocities required
	solver = rospy.ServiceProxy('vel_ik_server', Vel_IK)
	response = solver(q1, q2, q3, 0.0, 20.0, 0.0, 0.0, 0.0, 0.0)
	
	joint1_pub = rospy.Publisher('/rrbot/joint1_velocity_controller/command', Float64, queue_size=10)
	joint2_pub = rospy.Publisher('/rrbot/joint2_velocity_controller/command', Float64, queue_size=10)
	joint3_pub = rospy.Publisher('/rrbot/joint3_velocity_controller/command', Float64, queue_size=10)
	joint1_pub.publish(response.q1d)
	joint2_pub.publish(response.q2d)
	joint3_pub.publish(response.q3d)
	
	

rospy.init_node('straight_line')
rospy.Subscriber("joint_states", JointState, callback)
rospy.Subscriber("rrbot/joint2_velocity_controller/state", JointControllerState, c1)
rospy.spin()

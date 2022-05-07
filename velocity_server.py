#!/usr/bin/env python3

from rrbot_control.srv import Vel_FK, Vel_IK, Vel_FKResponse, Vel_IKResponse
import rospy
import math
import numpy as np

def forward(request):
	q1 = request.q1
	q2 = request.q2
	q3 = request.q3
	q1_dot = request.q1d
	q2_dot = request.q2d
	q3_dot = request.q3d
	
	J = [[-math.sin(q1+q2) - math.sin(q1), -math.sin(q1+q2), 0], [math.cos(q1+q2) + math.cos(q1), math.cos(q1+q2), 0], [0, 0, 1], [0, 0, 0], [0, 0, 0], [1, 1, 0]]
	q_dot = [[q1_dot], [q2_dot], [q3_dot]]
		
	ee_vel = np.around(np.matmul(J, q_dot),2)
	
	print(ee_vel)
	return Vel_FKResponse(ee_vel[0], ee_vel[1], ee_vel[2], ee_vel[3], ee_vel[4], ee_vel[5])
	
def inverse(request):
	q1 = request.q1
	q2 = request.q2
	q3 = request.q3
	vx = request.vx
	vy = request.vy
	vz = request.vz
	wx = request.wx
	wy = request.wy
	wz = request.wz
	
	J = [[-math.sin(q1+q2) - math.sin(q1), -math.sin(q1+q2), 0], [math.cos(q1+q2) + math.cos(q1), math.cos(q1+q2), 0], [0, 0, 1], [0, 0, 0], [0, 0, 0], [1, 1, 0]]
	
	ee_vel = [[vx], [vy], [vz], [wx], [wy], [wz]]
	
	q_dot = np.around(np.matmul(np.linalg.pinv(J), ee_vel),2)
	
	print(q_dot)
	
	return Vel_IKResponse(q_dot[0], q_dot[1], q_dot[2])

def server():
	rospy.init_node("velocity_server")
	rospy.Service('vel_fk_server', Vel_FK, forward)
	rospy.Service('vel_ik_server', Vel_IK, inverse)
	rospy.spin()

if __name__ == "__main__":
	server()


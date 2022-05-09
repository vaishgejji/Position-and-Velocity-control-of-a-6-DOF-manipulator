# Position-and-Velocity-control-of-a-6-DOF-manipulator

## Simulation of SCARA Robot

The simulation was created in Gazebo. To read the joint values from Gazebo, Joint State Publisher GUI was included in the launch file. Using these sliders, joint values can be manually set and are then published to the joint_state topic. 

## Forward Kinematics

Using the fk.py script, forward kinematics of the robot was solved. The script listens to the joint_state topic and calculates the end-effector position using the homogenous transformation matrix.

## Inverse Kinematics

ik_server.py calculates the joint values for the given values of position and orientation of the end-effector.

The use of socially assistive robots in Applied Behavioral Analysis (ABA) therapy has proven to help therapists focus more on the session rather than keeping a track of the child's progress. For this project, we consider ABA therapy sessions conducted for Autism Spectrum Disorder. The scenario considered here involves the use of PABI (Penguin for Autism Behavioral Intervention), a socially assistive robot created specifically to assist  in ABA therapies. It is equipped with Intel REalSense camera which is used for data recording, data logging and further analysis. Face and pose recognition can help determine behavioral aspects of patients during ABA therapy. 


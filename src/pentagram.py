#! /usr/bin/env python

import rospy                               # Import the Python library for ROS
from geometry_msgs.msg import Twist            # Import the Twist message from the geometry_msg package
import math

rospy.init_node('penta')                # Initiate a Node named 'infinity_node'
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)    # Create a Publisher object, that will publish on the /cmd_vel topic
                                           #  messages of type Twist

rate = rospy.Rate(1)                   # Set a publish rate of 2 Hz
msg = Twist()                              # Create a var of type Tist

x=True

while not rospy.is_shutdown():             # Create a loop that will go until someone stops the program execution
    if (x==True):
        x=False
        msg.angular.z=0
        msg.linear.x=1
    else:
        x=True
        msg.linear.x=0
        msg.angular.z = (0.8*math.pi)
    pub.publish(msg)
    
    rate.sleep()
    
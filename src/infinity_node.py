#! /usr/bin/env python

import rospy                               # Import the Python library for ROS
from geometry_msgs.msg import Twist            # Import the Twist message from the geometry_msg package
import math

rospy.init_node('infinity')                # Initiate a Node named 'infinity_node'
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)    # Create a Publisher object, that will publish on the /cmd_vel topic
                                           #  messages of type Twist

rate = rospy.Rate((1/(8*math.pi)))                   # Set a publish rate of 2 Hz
msg = Twist()                              # Create a var of type Tist

msg.angular.z = 0.25
msg.linear.x = -.5

while not rospy.is_shutdown():             # Create a loop that will go until someone stops the program execution
    pub.publish(msg)
    msg.angular.z = -msg.angular.z
    rate.sleep()
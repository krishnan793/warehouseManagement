#!/usr/bin/env python

# This node will perform a search pattern
# 
# Author : Ananthakrishnan U S

import roslib
# ardrone_tutorials has a good ardrone classs for controlling drone. load_manifest import that python module
roslib.load_manifest("ardrone_control")

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from visualization_msgs.msg import Marker
from drone_controller import BasicDroneController
import time




def reset_drone(pub1):
	controller.SetCommand(0,0,0,0)
	time.sleep(1)

def search_pattern():
	controller.SetCommand(0,0,0.2,0)
	sleep(1)
	controller.SetCommand(0,0,0,0)
	sleep(1)

if __name__ == '__main__':
	rospy.init_node('autonomous_search', anonymous=True)
	pub1 = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	controller = BasicDroneController()
	controller.StartSendCommand()
	rospy.sleep(2.0)
	controller.SendTakeoff()
	rospy.sleep(5.0)
	controller.SetCommand(0,0,0,1)
	rospy.sleep(5.0)
	controller.SetCommand(0,0,0,-1)
	rospy.sleep(2.0)
	controller.SendLand()
	#controller.StartSendCommand()
	#search_pattern()
	#reset_drone(pub1)
	rospy.spin()
	



#!/usr/bin/env python

# This node will perform a lawn mower search pattern unti a tag is detected
# https://github.com/krishnan793/ar2landing_neural
# Author : Ananthakrishnan U S

import roslib
# ardrone_tutorials has a good ardrone classs for controlling drone. load_manifest import that python module
roslib.load_manifest("ardrone_control")

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
#from visualization_msgs.msg import Marker
from drone_controller import BasicDroneController
import time



def detect_tag(data):
	# This will set a flag and stop executing autonomous search
	controller.SetCommand(0,0,0,0)
	controller.StopSendCommand()
	global detect
	detect = 1

def sleep(sec):
	while(sec and not rospy.is_shutdown()):
		if(detect==1):
			break
		time.sleep(1)
		sec -= 1

def reset_drone(pub1):
	controller.SetCommand(0,0,0,0)
	time.sleep(1)

def search_pattern():
	controller.SetCommand(0,0,0,0)
	time.sleep(0.5)
	controller.SetCommand(0,0,0,0)
	time.sleep(0.5)
	while not rospy.is_shutdown() and detect == 0:
		controller.SetCommand(0,1,0,0)
		sleep(1)
		controller.SetCommand(-1,0,0,0)
		sleep(9)
		controller.SetCommand(0,1,0,0)
		sleep(1)
		controller.SetCommand(1,0,0,0)
		sleep(9)

def move(x,y,z,theta):
    scale = 1
    a0 = 0.2

    a1 = a0
    a2 = (a1*y/x)
    a3 = (a1*z/x)

    controller.SetCommand(a1,a2,a3,theta)
    

def zigzag():

    #print "Forward"
    #controller.SetCommand(0,0.15,0,0)
    #rospy.sleep(2)
    #print "Stop"
    #controller.SetCommand(0,0,0,0)
    #rospy.sleep(1)

    #print "Up"
    #controller.SetCommand(0,0,0,0.25)
    #rospy.sleep(1.5)
    #print "Stop"
    #controller.SetCommand(0,0,0,0)
    #rospy.sleep(1)

    #print "Forward"
    #controller.SetCommand(0,0.15,0,0)
    #rospy.sleep(2)
    #print "Stop"
    #controller.SetCommand(0,0,0,0)
    #rospy.sleep(1)

    print "Left"
    controller.SetCommand(0.25,0,0,0)
    rospy.sleep(1.5)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(5)

    print "Up"
    controller.SetCommand(0,0,0,0.25)
    rospy.sleep(3)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(1)

    print "Right"
    controller.SetCommand(-0.25,0,0,0)
    rospy.sleep(1.5)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(1)

    #print "Up"
    #controller.SetCommand(0,0,0,0.25)
    #rospy.sleep(2.5)
    #print "Stop"
    #controller.SetCommand(0,0,0,0)
    #rospy.sleep(1)

    #print "Left"
    #controller.SetCommand(0.25,0,0,0)
    #rospy.sleep(1)
    #print "Stop"
    #controller.SetCommand(0,0,0,0)
    #rospy.sleep(5)


    print "Down"
    controller.SetCommand(0,0,0,-0.3)
    rospy.sleep(3)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(1)
    

    #print "Down"
    #controller.SetCommand(0,0,0,-0.15)
    #rospy.sleep(2)
    #print "Stop"
    #controller.SetCommand(0,0,0,0)
    #rospy.sleep(1)
    
    #print "Backward"
    #controller.SetCommand(0,-0.25,0,0)
    #rospy.sleep(2)
    #print "Stop"
    #controller.SetCommand(0,0,0,0)
    #rospy.sleep(1)
    

def zigzag2():

    print "Left"
    controller.SetCommand(0.25,0,0,0)
    rospy.sleep(1.5)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(5)

    print "Left"
    controller.SetCommand(0.25,0,0,0)
    rospy.sleep(2)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(5)

    print "Up"
    controller.SetCommand(0,0,0,0.25)
    rospy.sleep(3.5)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(1)

    print "Right"
    controller.SetCommand(-0.25,0,0,0)
    rospy.sleep(2)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(2)

    print "Right"
    controller.SetCommand(-0.25,0,0,0)
    rospy.sleep(1.6)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(2)

    print "Down"
    controller.SetCommand(0,0,0,-0.3)
    rospy.sleep(3)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(1)
    
def square():

    print "Right"
    controller.SetCommand(-0.25,0,0,0)
    rospy.sleep(1.5)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(1)

    print "Up"
    controller.SetCommand(0,0,0,0.25)
    rospy.sleep(3)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(1)

    print "Left"
    controller.SetCommand(0.25,0,0,0)
    rospy.sleep(1.5)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(5)

    print "Down"
    controller.SetCommand(0,0,0,-0.3)
    rospy.sleep(3)
    print "Stop"
    controller.SetCommand(0,0,0,0)
    rospy.sleep(1)



if __name__ == '__main__':
    rospy.init_node('preplanned_path', anonymous=True)
    pub1 = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=10)
    controller = BasicDroneController()
    controller.StartSendCommand()
    rospy.sleep(1)

    controller.SendTakeoff()
    print "Take off"
    controller.StartSendCommand()
    rospy.sleep(5)

    zigzag2()
    
    print "Down"
    controller.SetCommand(0,0,0,-0.25)
    rospy.sleep(3)

    #rospy.sleep(1)
    print "Land"
    controller.SendLand()

    #pub2 = rospy.Subscriber("/visualization_marker", Marker, detect_tag)
    #search_pattern()
    #reset_drone(pub1)
    #rospy.spin()



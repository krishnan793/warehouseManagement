#!/usr/bin/env python

# This node will perform a search pattern
# 
# Author : Ananthakrishnan U S

import roslib
# ardrone_tutorials has a good ardrone classs for controlling drone. load_manifest import that python module
#roslib.load_manifest("ardrone_control")

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from std_msgs.msg import String
from visualization_msgs.msg import Marker
#from drone_controller import BasicDroneController
import time
from sensor_msgs.msg import Image
from sys import argv
import zbar
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy
import Image as Image2
from rospy.numpy_msg import numpy_msg
from qrcode_zbar.msg import qrcode

def image_callback(msg):
	print chr(27)+"[2J"
	if(msg.qrcode=='100003'):
		print chr(27)+"[H"
		print chr(27)+"[31mTV"+chr(27)+"[39m"
	if(msg.qrcode=='100004'):
                print chr(27)+"[H"
                print chr(27)+"[31mFridge"+chr(27)+"[39m"


if __name__ == '__main__':
	#rospy.init_node('qrcode_reader', anonymous=True)
	rospy.init_node('qrcode_listener')

	# Set up your subscriber and define its callback
	rospy.Subscriber('/qr_code', qrcode, image_callback)
	
	rospy.spin()
	



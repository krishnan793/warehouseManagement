#!/usr/bin/env python

# This node will perform a search pattern
# 
# Author : Ananthakrishnan U S

import roslib
# ardrone_tutorials has a good ardrone classs for controlling drone. load_manifest import that python module
#roslib.load_manifest("ardrone_control")

import rospy
from sys import argv
from qrcode_zbar.msg import qrcode


Database_QRCode = {'Box - 1':[False,0,0,1,0,0],
		'Box - 2':[False,1,0,0,0,0],
		'Box - 3':[False,0,1,0,0,0],
		'Box - 4':[False,0,0,0,0,1],
		'Box - 5':[False,0,0,0,1,0],
		'Box - 6':[False,0,0,1,0,0]
		}

dict = {'item1': 0, 'item2': 0, 'item3': 0, 'item4': 0, 'item5': 0}

def callback(data):
	global Database_QRCode

	if not data.qrcode in Database_QRCode:
		return
	if Database_QRCode[data.qrcode][0]:
		return
	else:
		wms_frontend(data.qrcode)

def wms_frontend(qrcode,reset = 0):
	global Database_QRCode
	Database_QRCode[qrcode][0] = True
	global dict

	for index, val in enumerate(Database_QRCode[qrcode][1:]):
		dict['item'+str(index+1)] += val

	if reset==1:
		dict = {'item1': 0, 'item2': 0, 'item3': 0, 'item4': 0, 'item5': 0}

	print "\t\t"+chr(27)+"[2J"+chr(27)+"[H"
	print "\t\t"+chr(27)+"[47m"+chr(27)+"[30mSerial No:\t\tProduct\t\tInStock"+chr(27)+"[39m"+chr(27)+"[49m"

	for i in range(0,5):
		print "\t\t"+str(i+1)+"\t\t\tSKU"+str(i+1)+"\t\t",dict['item'+str(i+1)]

	print "\n\n " + qrcode + "\n---------" 
	for index, val in enumerate(Database_QRCode[qrcode][1:]):
		print "SKU"+str(index+1)," : ",val

if __name__ == '__main__':
	#rospy.init_node('qrcode_reader', anonymous=True)
	rospy.init_node('qrcode_listener')

	# Set up your subscriber and define its callback
	rospy.Subscriber('/qr_code', qrcode, callback)
	
	rospy.spin()
	

'''
print chr(27)+"[2J"
if(data.qrcode=='100003'):
	print chr(27)+"[H"
	print chr(27)+"[31mTV"+chr(27)+"[39m"
if(data.qrcode=='100004'):
        print chr(27)+"[H"
        print chr(27)+"[31mFridge"+chr(27)+"[39m"

'''

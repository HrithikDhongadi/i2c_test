#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from smbus import SMBus

addr = 0x8 # bus Address

bus = SMBus(0)

def callback(data):
    rospy.loginfo("I heard %s", data.data)
    ledstate = data.data

    if ledstate=="1":
        bus.write_byte(addr,0x1)
        rospy.loginfo("LED ON")

    elif ledstate=="0":
        bus.write_byte(addr,0x0)
        rospy.loginfo("LED OFF")

    else:
        pass
    

def i2c_receiver():
    rospy.init_node('i2c_receiver', anonymous=True)
    sub = rospy.Subscriber('i2c_line',String, callback)
    rospy.spin()

if __name__ == '__main__':
    i2c_receiver()
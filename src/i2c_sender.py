#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def i2c_sender():
    pub =rospy.Publisher('i2c_line', String, queue_size=10)
    rospy.init_node('i2c_sender',anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        str = '1'
        rospy.loginfo(str)
        pub.publish(str)
        rate.sleep()

        str = '0'
        rospy.loginfo(str)
        pub.publish(str)
        rate.sleep()


if __name__ == '__main__':
    try:
        i2c_sender()
    except rospy.ROSInterruptException:
        pass
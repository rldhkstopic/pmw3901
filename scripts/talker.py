#!/usr/bin/env python

import rospy
import time
import argparse

from std_msgs.msg import String
from math import sqrt, cos, sin, pi
from pmw3901 import PMW3901, BG_CS_FRONT_BCM

SensorClass = PMW3901
flo = SensorClass(spi_port=0, spi_cs=1, spi_cs_gpio=BG_CS_FRONT_BCM)
flo.set_rotation(0)


tx, ty = (0,0)

rospy.init_node('talker', anonymous=True)
pub = rospy.Publisher('chatter', String, queue_size=10)
rate = rospy.Rate(1) # 10hz

if __name__ == '__main__':
    while not rospy.is_shutdown():
      currentTime = rospy.Time.now()
      try:
        opt_x, opt_y = flo.get_motion()
      except RuntimeError:
        continue
      
      
      if opt_x > 100 : opt_x = 0
      if opt_y > 100 : opt_y = 0

      tx += x; ty += y
      
      dt = (currentTime - lastTime).to_sec()
      distance = sqrt(abs((tx*tx) - (ty*ty))) * 3.10
  
      # local_x = opt_x + cos(opt_y) * dist
      # local_y = opt_x + sin(opt_y) * dist
      # local_z = opt_y + dist / 0.093

     
      lastTime = rospy.Time.now()

      pub.publish("ABS|{:03d}|{:03d}|DIST|{:01f}".format(tx, ty, distance))
      rate.sleep()

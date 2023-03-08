#!/usr/bin/env python3

import sys
import rclpy
#sys.path.append(".")
sys.path.append("./..")
from std_srvs.srv import Empty
from std_msgs.msg import String
from smap_classification_wrapper.classification_wrapper import classification_wrapper


class classifier_1(classification_wrapper):

    def __init__(self,node_name):
        super().__init__(node_name)
        self.srv = self.create_service(Empty, 'test_service', callback=self.service_callback, callback_group=self.reentrant_cb_group)

    def service_callback(self, request, result):
        self.get_logger().info('------------------------------------Received request, responding...')
        return result

    #def timer_callback(self):
    #    msg = String()
    #    msg.data = 'Hello World-1: %d' % self.i
    #    self.publisher_.publish(msg)
    #    self.get_logger().info('Publishing: "%s"' % msg.data)
    #    self.i += 1
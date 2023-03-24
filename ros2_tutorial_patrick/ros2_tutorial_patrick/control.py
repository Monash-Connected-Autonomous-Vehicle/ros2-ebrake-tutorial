# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool



class Control(Node):

    def __init__(self):
        super().__init__('control')
        self._break_active = False
        self.subscriber = self.create_subscription(Bool, '/ebrake_is_active', self._break_car, 10)
        self._publisher = self.create_publisher(Twist, '/simulated_vehicle/cmd_vel', 10)

        timer_period = 0.5  # seconds
        self.acc_timer = self.create_timer(timer_period, self._acc_callback)

    def _acc_callback(self):
        if not self._break_active:
            self._drive_command({
                    "x": 1,
                    "y": 0,
                    "z": 0
                })

    def _break_car(self, break_msg):
        self._break_active = break_msg.data
        if self._break_active:
            self._drive_command({
                "x": 0,
                "y": 0,
                "z": 0
            })

    def _drive_command(self, linear_acc, angular_acc={"x": 0, "y": 0, "z": 0}):
        # vectors in dict form
        drive_msg = Twist()
        drive_msg.linear.x = float(linear_acc["x"])
        drive_msg.linear.y = float(linear_acc["y"])
        drive_msg.linear.z = float(linear_acc["z"])

        drive_msg.angular.x = float(angular_acc["x"])
        drive_msg.angular.y = float(angular_acc["y"])
        drive_msg.angular.z = float(angular_acc["z"])
        self._publisher.publish(drive_msg)



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Control()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

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
import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2
# from sensor_msgs im port PointCloud2 as pc2
from sensor_msgs_py import point_cloud2
from std_msgs.msg import Bool

class Sense(Node):

    def __init__(self):
        super().__init__('sense')
        self._msg = Bool()
        self._subscriber = self.create_subscription(PointCloud2, '/lidar/points', self._points_callback, 10)
        self._publisher = self.create_publisher(Bool, '/ebrake_is_active', 10)      

    def _points_callback(self, points_msg):
        points = point_cloud2.read_points_list(points_msg)
        STOPPING_DISTANCE = 5
        # MARGIN_FOR_ERROR = 4160
        MARGIN_FOR_ERROR = 0
        points_too_close = 0
        for point in points:
            if self._is_valid_point(point):
                points_too_close += 1

        if points_too_close > MARGIN_FOR_ERROR: # arbitrary margin for error
            self._msg.data = True
        else:
            self._msg.data = False

        self._publisher.publish(self._msg) # change depending on point cloud

    def _absolute_distance_from_point(self, point):
        x = point.x
        y = point.y
        z = point.z
        return math.sqrt(x**2 + y**2 + z**2)

    def _is_valid_point(self, point):
        if point.y < 0.5 and point.y > -0.5 and point.x > 0 and point.x < 5 and point.z < 1:
            self.get_logger().info(f"x: {point.x} y: {point.y} z: {point.z}")
            return True

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Sense()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

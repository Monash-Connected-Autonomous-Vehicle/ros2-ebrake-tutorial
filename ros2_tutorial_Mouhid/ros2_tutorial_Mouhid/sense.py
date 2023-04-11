import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Bool
from sensor_msgs_py import point_cloud2 as pc2
import math

class SenseNode(Node):
    def __init__(self):
        super().__init__('sense_node')
        self.publisher_ = self.create_publisher(Bool, '/ebrake_is_active', 10)
        self.subscription_ = self.create_subscription(
            PointCloud2,
            '/lidar/points',
            self.pointcloud_callback,
            10
        )
        self.distance_threshold_ = 5.0  # distance threshold in meters

    def pointcloud_callback(self, msg):
        # Read points from PointCloud2 message
        points = pc2.read_points_list(msg)

        # Check for obstacles within the distance threshold
        obstacle_detected = False
        for point in points:
            if point.x > 0:
                if abs(point.y) < 0.5:
                    distance = math.sqrt(point[0] ** 2 + point[1] ** 2 + point[2] ** 2)
                    if 1 < distance < self.distance_threshold_:
                        obstacle_detected = True
                        break

        # Publish the emergency brake status
        ebrake_msg = Bool()
        ebrake_msg.data = obstacle_detected
        self.publisher_.publish(ebrake_msg)
        if obstacle_detected:
            self.get_logger().info('Emergency brake is active: obstacle detected!')
        else:
            self.get_logger().info('Emergency brake is inactive: no obstacle detected.')

def main(args=None):
    rclpy.init(args=args)
    node = SenseNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


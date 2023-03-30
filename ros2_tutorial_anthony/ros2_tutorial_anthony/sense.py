import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Bool
from sensor_msgs_py import point_cloud2 as pc2


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('ebrake_sense')
        self.publisher_ = self.create_publisher(Bool, '/ebrake_is_active', 10)
        self.subscription = self.create_subscription(
            PointCloud2,
            '/lidar/points',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.pc2 = []        

    def listener_callback(self, msg):
        self.pc2 = pc2.read_points_list(msg)
        self.get_logger().info('I received lidar data')
        
    def timer_callback(self):
        msg = Bool()
        msg.data = False
        dist = None
        for point in self.pc2:
            dist = (point.x**2 + point.y**2 + point.z**2)**0.5
            if 1 < dist < 5:
                msg.data = True
                break
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s" m away' % str((msg.data, dist)))
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

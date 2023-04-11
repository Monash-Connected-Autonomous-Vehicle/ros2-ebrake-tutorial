import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
from std_msgs.msg import Bool
import math


class ControlNode(Node):

    def __init__(self):
        super().__init__('control_node')
        self.publisher_ = self.create_publisher(TwistStamped, '/simulated_vehicle/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Bool, '/ebrake_is_active', self.listener_callback, 10)
        self.emergency_brake = False
        self.timer = self.create_timer(1, self.publish_twist)

    def listener_callback(self,msg):
        self.emergency_brake = msg.data # Gets brake data

    def publish_twist(self):
        msg = TwistStamped()
        if not self.emergency_brake:
            msg.twist.linear.x = 2.0  # forward
            self.publisher.publish(msg)
  
        else:
            msg.twist.linear.x= 0.0
            msg.twist.angular.x = 0.0
            print("Stop")
            self.publisher.publish(msg)




def main(args=None):
    rclpy.init(args=args)
    control_node = ControlNode()
    rclpy.spin(control_node)
    control_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

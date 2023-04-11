import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
import math

class ControlNode(Node):

    def __init__(self):
        # Initialize the ROS2 node
        
        super().__init__('control_node')

        # Create a publisher with the desired topic name and message type
        self.publisher = self.create_publisher(Twist, '/simulated_vehicle/cmd_vel', 10)
        
        #Create a subscriber for the emergency brake status
        self.subscription = self.create_subscription(
            Bool,
            '/ebrake_is_active',
             self.ebrake_callback,
            10)
        self.ebrake_active = False
        self.timer = self.create_timer(1, self.publish_twist)
        
        
    def ebrake_callback(self,msg):
        #Global variable to store the emergency brake status
        self.ebrake_active = msg.data
        
    def publish_twist(self):
    # Publish Twist messages repeatedly at a rate of 0.2 Hz
        msg = Twist()
        if not self.ebrake_active:
            # Command 1: Drive forwards
            msg.linear.x = 2.0  # linear velocity in the x-axis
            msg.angular.z = 0.0  # angular velocity in the z-axis
            self.publisher.publish(msg)
            self.get_logger().info('Publishing: Drive forwards')
        else:
            # Command 2: Stop
            msg.linear.x = 0.0  # stop linear velocity
            msg.angular.z = 0.0  # angular velocity for rotation in the z-axis
            self.publisher.publish(msg)
            self.get_logger().info('Publishing: Stop')
    

def main(args=None):
    rclpy.init(args=args)
    control_node = ControlNode()
    rclpy.spin(control_node)
    # Clean up
    control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



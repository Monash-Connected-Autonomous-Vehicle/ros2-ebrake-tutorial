import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('control_vel')
        self.publisher_ = self.create_publisher(Twist, '/simulated_vehicle/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Bool
        ,'/ebrake_is_active'
        ,self.listener_callback
        , 10
        )
        timer_period = 5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.e_brake = False

    def listener_callback(self,msg):
    	self.e_brake = msg.data
    	self.get_logger().info('I received E-brake is %s' %msg.data)
    
    def timer_callback(self):
        msg = Twist()
        if not self.e_brake:
            msg.linear.x = 3.0
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: Linear x and Angular z:  %s' % str((msg.linear.x,msg.angular.z)))
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('Ebrake is active')
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

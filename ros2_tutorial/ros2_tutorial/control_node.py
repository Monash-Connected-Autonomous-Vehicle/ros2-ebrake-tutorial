import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Control(Node):

    def __init__(self):
        super().__init__('task1')
        self.drive_publisher_ = self.create_publisher(Twist,"cmd_vel",10)
        timer_period = 5
        self.drive_timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('publishing twist message')
        '''
        - Create empty Twist message
        - Change linear velocity
        - Publish message
        '''
    
def main(args=None):
    rclpy.init(args=args)
    control = Control()
    rclpy.spin(control)

    control.destroy_node()
    rclpy.shutdown()

if __name__=="main":
    main()




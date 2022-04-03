import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Task1(Node):

    def __init__(self):
        super().__init__('task1')
        self.drive_publisher_ = self.create_publisher(Twist,"cmd_vel",10)
        timer_period = 5
        self.drive_timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('test')

    def timer_callback(self):
        self.get_logger().info('test')
        '''
        Prefill a Twist Message Here to publish 
        '''
    
def main(args=None):
    rclpy.init(args=args)
    task1 = Task1()
    task1.destroy_node()
    rclpy.spin(task1)
    rclpy.shutdown()

if __name__=="main":
    main()




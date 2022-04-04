import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Control(Node):

    def __init__(self):
        super().__init__('control')
        '''
        - Create a publisher for /cmd_vel
        - Create a timer_callback where you will publish velocity
        '''

    def timer_callback(self):
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




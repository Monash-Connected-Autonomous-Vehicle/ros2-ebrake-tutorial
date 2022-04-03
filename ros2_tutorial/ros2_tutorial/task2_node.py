import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Range

class Task2(Node):

    def __init__(self):
        super().__init__('task2')
        self.ebrake_publisher_ = self.create_publisher(Twist,"cmd_vel",10)
        self.laser_subscriber_ = self.create_subscription(Range, 'laser/range', self.callback, 10)
        self.get_logger().info('task2')

    def callback(self, msg: Range):
        '''
        Implement logic to stop the car when there is an obstacle within 5 meters of it
        '''
        
    
def main(args=None):
    rclpy.init(args=args)
    task2 = Task2()
    rclpy.spin(task2)

    task2.destroy_node()
    rclpy.shutdown()

if __name__=="main":
    main()




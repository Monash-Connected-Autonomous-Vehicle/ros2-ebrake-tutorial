import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Range
from std_msgs.msg import Bool
from nav_msgs.msg import Odometry

class Sense(Node):

    def __init__(self):
        super().__init__('sense')
        self.ebrake_publisher_ = self.create_publisher(Bool,"/e_brake",10)
        self.laser_subscriber_ = self.create_subscription(Range, 'laser/range', self.laser_callback, 10)
        self.range_detected = ""

    def laser_callback(self, msg: Range):
        '''
        Set range_detected
        Send emergency brake signal if range_detected is less than a threshold
        '''

def main(args=None):
    rclpy.init(args=args)
    sense = Sense()
    rclpy.spin(sense)

    sense.destroy_node()
    rclpy.shutdown()

if __name__=="main":
    main()




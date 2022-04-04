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
        '''
        Create a subscriber for /laser/range
        Create a publisher to publish to /e_brake. This should be a Bool message type 
        Initialise a range_detected variable you can update 
        '''

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




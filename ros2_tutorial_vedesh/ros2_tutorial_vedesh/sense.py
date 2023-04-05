import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2 as pc2


class SenseNode(Node):

    def __init__(self):
        super().__init__('sense_node')
        self.subscription = self.create_subscription(
            PointCloud2, '/lidar/points', self.listener_callback, 10)
        self.publisher = self.create_publisher(Bool, '/ebrake_is_active', 10)
        self.timer = self.create_timer(1,self.callback)
        self.points = []

    def listener_callback(self,msg):
        self.points = pc2.read_points_list(msg) # Gets lidar data
        print("Obtained Lidar data")

    def callback(self):
        msg = Bool()
        msg.data = False
        for p in self.points:
            if p.x > 0:
                if abs(p.y)<0.5:
                    dist = (p.x**2 + p.y**2)**0.5 # if obstacle within 5m radius
                    if 1 < dist < 5:
                        print("Object Detected")
                        msg.data = True
                        break
        self.publisher.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    sense_node = SenseNode()
    rclpy.spin(sense_node)
    sense_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

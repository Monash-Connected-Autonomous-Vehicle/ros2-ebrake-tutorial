#include "ros/ros.h"
#include "geometry_msgs/Twist.h"


int main(int argc, char **argv)
{

  // ros setup
  ros::init(argc, argv, "donuts");
  ros::NodeHandle nh;

  // logging message
  ROS_INFO("Initialised Control Node: Doing Donuts");
  
  // setup publisher
  ros::Publisher control_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 10);

  ros::Rate loop_rate(10);


  geometry_msgs::Twist msg;

  // set linear and angular velocity 
  msg.linear.x = 0.22; // 0.22 is max speed
  msg.angular.z = 0.5;

  // continuously publish twist
  while (ros::ok())
  {

    // publish control message
    control_pub.publish(msg);


    ros::spinOnce();

  }


  return 0;
}

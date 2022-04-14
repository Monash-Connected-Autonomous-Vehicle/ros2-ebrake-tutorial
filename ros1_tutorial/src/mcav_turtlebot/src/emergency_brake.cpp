
#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "geometry_msgs/Twist.h"

class EmergencyBrake
{
  public:

  EmergencyBrake() 
  {

    // get stopping distance param
    ros::param::get("/stop_distance", stop_distance_);
    ROS_INFO("Stopping Distance set at %d m", stop_distance_);

    // laser subscriber
    laser_sub_ = nh_.subscribe("/scan", 10, &EmergencyBrake::LaserCallback, this);


    // control publisher
    control_pub_ = nh_.advertise<geometry_msgs::Twist>("/cmd_vel", 10);

  }

  void LaserCallback(const sensor_msgs::LaserScan::ConstPtr& msg)
  {

    // setup twist message
    geometry_msgs::Twist twist;
    twist.angular.z = 0.0;


    if(!(msg->ranges.empty())) {

      // only check the scan directly infront of turtlebot. layout is (0 - 360)
      if (msg->ranges[0] < stop_distance_) {

        // object detected at close range, stop the vehicle
        ROS_INFO("Stopping the vehicle... %f m to object.", msg->ranges[0]);
        twist.linear.x = 0.0;

      } else {

        // no object detected at close range, continue driving
        ROS_INFO("Continue Driving... %f m to object.", msg->ranges[0]);
        twist.linear.x = 0.22;

      }

    } else{

        ROS_INFO("No Laser Data Received...");

    }

    // publish twist message
    control_pub_.publish(twist);
}

private:
  ros::NodeHandle nh_; 
  ros::Publisher control_pub_;
  ros::Subscriber laser_sub_;

  double stop_distance_ = 1.0;

};


int main(int argc, char **argv)
{

  ros::init(argc, argv, "emergency_brake");

  EmergencyBrake EmBrake;

  ros::spin();

  return 0;
}



// https://answers.ros.org/question/60239/how-to-extract-and-use-laser-data-from-scan-topic-in-ros-using-c/
// https://get-help.robotigniteacademy.com/t/how-to-read-the-laserscan-store-and-display-it-simultaneously-topics-quiz/990/7
// https://answers.ros.org/question/59725/publishing-to-a-topic-via-subscriber-callback-function/
# ros2-ebrake-tutorial

Lidar tf frame: `/vehicle_blue/lidar_link/gpu_lidar`

# Running
Run gazebo: `ign gazebo -v 4 -r /home/mcav/mcav_ws/src/ros2_tutorial/lidar_playground.sdf`
Run topic bridge: `ros2 run ros_gz_bridge parameter_bridge --ros-args -p config_file:=$HOME/mcav_ws/src/ros2_tutorial/gazebo_topics.yaml`

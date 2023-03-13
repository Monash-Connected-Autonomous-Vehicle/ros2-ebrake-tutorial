# ros2-ebrake-tutorial

Lidar tf frame: `/vehicle_blue/lidar_link/gpu_lidar`

# Installing and building
### Make sure to create a workspace
E.g.
```
cd ~
mkdir -p tutorial_ws/src
```
### Download the code

```
cd ~/tutorial_ws/src
git clone git@github.com:Monash-Connected-Autonomous-Vehicle/ros2-ebrake-tutorial.git
```

### Build all the code in the workspace

```
cd ~/tutorial_ws
colcon build
```

# Running

Please open a new terminal window or tab. With ROS2, you don't want to run code in the same terminal that you built it.

```
cd ~/tutorial_ws
. install/setup.bash
ros2 launch simulation_launch gazebo_playground.launch
```

Run gazebo: `ign gazebo -v 4 -r /home/mcav/mcav_ws/src/ros2_tutorial/lidar_playground.sdf`
Run topic bridge: `ros2 run ros_gz_bridge parameter_bridge --ros-args -p config_file:=$HOME/mcav_ws/src/ros2_tutorial/gazebo_topics.yaml`

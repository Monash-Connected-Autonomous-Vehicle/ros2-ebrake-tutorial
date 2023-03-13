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

You should see the Gazebo simulator open to a view like this:
![image](https://user-images.githubusercontent.com/7232997/224651017-a36d1cac-096e-4d8c-aabe-47a4e6fb09dc.png)

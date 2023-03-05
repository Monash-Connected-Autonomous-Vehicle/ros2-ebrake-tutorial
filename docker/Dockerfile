FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-ros-gz \
    && rm -rf /var/lib/apt/lists/*
    
RUN apt-get update && apt-get install -y \
    tmux \
    vim \
    ros-humble-gazebo-dev \
    ros-humble-gazebo-ros-pkgs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/$USERNAME/mcav_ws/src
RUN git clone https://github.com/ToyotaResearchInstitute/velodyne_simulator.git


# Create a non-root user with sudo privileges
ARG USERNAME=mcav
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Add tmux configuration file
COPY docker/.tmux.conf /home/${USERNAME}/.tmux.conf

WORKDIR /home/$USERNAME/mcav_ws/src/ros2_tutorial
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /home/${USERNAME}/.bashrc
CMD /bin/bash
USER $USERNAME
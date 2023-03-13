FROM osrf/ros:humble-desktop
    
RUN apt-get update && apt-get install -y \
    tmux \
    vim \
    ros-humble-ros-gz \
    ros-humble-gazebo-dev \
    ros-humble-gazebo-ros-pkgs \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user with sudo privileges
ARG USERNAME=mcav
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
USER $USERNAME

# Add tmux configuration file
COPY docker/.tmux.conf /home/${USERNAME}/.tmux.conf

RUN mkdir -p /home/${USERNAME}/mcav_ws/src
WORKDIR /home/${USERNAME}/mcav_ws/src
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /home/${USERNAME}/.bashrc
CMD /bin/bash
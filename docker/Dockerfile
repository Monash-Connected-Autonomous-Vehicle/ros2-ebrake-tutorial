FROM ros:humble
    
RUN apt-get update && apt-get install -y \
    tmux \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null \
    && apt-get update && apt-get install -y \
    gz-garden \
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
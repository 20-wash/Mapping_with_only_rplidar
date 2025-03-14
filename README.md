# Mapping_with_only_rplidar

## Overview
A ROS 2-based package for mapping using **RPLiDAR** and **RF2O laser odometry**. This repository integrates RPLiDAR for scanning and RF2O for odometry estimation, allowing autonomous mapping in an environment.

This is a package that make the 2D map of the environment with the help of RP lidar only. It only require RP Lidar to create the map. Instead you don't have the lidar, the bag file is attached herewith. 


## 🛠 Features
- **LIDAR-based Mapping**: Uses RPLiDAR for 2D mapping.
- **Odometry Estimation**: Implements RF2O laser odometry.
- **ROS 2 Integration**: Works with ROS 2 Humble.
- **Customized Launch Files**: Optimized for RPLiDAR A1.

## 📂 Repository Structure
```bash
map_rplidar/
├── src/
│   ├── rplidar_ros/            # Forked ; Publish /scan topic in "laser" frame
│   ├── transforms/             # Package that launch static transformations necessary for the slam toolbox
│   ├── rf2o_laser_odometry/    # Forked and modified; Publish /odom topic in "odom" frame  
│   ├── mapping_bringup/        # This launches all the node in once.  
```



## 🚀 Installation

### 1️⃣ Clone the Repository
```bash
git clone --recurse-submodules https://github.com/20-wash/map_rplidar.git
cd map_rplidar
```

### 2️⃣ Install the Dependencies
```bash
sudo apt update
sudo apt install -y ros-humble-slam-toolbox
```

### 3️⃣ Build the Package
```bash
colcon build --symlink-install
source install/setup.bash
```

### ▶️ Running the Lauch File (If there is LiDAR)
```bash
ros2 launch mapping_bringup rp_lidar_slam_launch.py 
```

### ▶️ Running the Lauch File (From BAG file)
```bash
ros2 launch mapping_bringup bag_rp_lidar_slam_launch.py 
```
This plays the bag file, (the bag play rate is set as 0.1)

Launching the launch file
![alt text](image.png)


Visualization in rviz. The rviz config is saved inside (rviz) folder inside mapping_bringup package. 
![alt text](image-1.png)
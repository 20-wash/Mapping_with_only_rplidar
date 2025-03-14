from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Arguments
    rosbag_file = DeclareLaunchArgument("rosbag_file", default_value="/home/biswash/Desktop/bag's/rosbag2/rosbag2_2024_12_14-rp_lidar/rosbag2_2024_12_14-10_04_52_0.db3", description="Path to the ROS2 bag file")
    playback_rate = DeclareLaunchArgument("playback_rate", default_value="0.1", description="Rate to play the bag file (0.1)")
    rviz_config_file = DeclareLaunchArgument("rviz_config_file", default_value="/home/biswash/workspace/map_rplidar/src/mapping_bringup/rviz/default_for_package.rviz", description="Path to the RViz configuration file")
    
    # Start bag playback without publishing clock
    rosbag_play = ExecuteProcess(
        cmd=['ros2', 'bag', 'play', LaunchConfiguration("rosbag_file"), 
             '--topics', '/scan',
             '--rate', LaunchConfiguration("playback_rate"),
             '--loop'],  # Loop playback, but no --clock option
        output='screen'
    )
    
    # Static Transforms - with delay
    transforms_action = TimerAction(
        period=2.0,  # Wait 2 seconds before launching transforms
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource('/home/biswash/workspace/map_rplidar/src/transforms/launch/tf_setup_launch.py')
            )
        ]
    )
    
    # Odometry with delay
    odometry_action = TimerAction(
        period=3.0,  # Wait 3 seconds before launching odometry
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource('/home/biswash/workspace/map_rplidar/src/rf2o_laser_odometry/launch/rf2o_laser_odometry.launch.py')
            )
        ]
    )
    
    # SLAM Toolbox with delay - now using real time
    slam_action = TimerAction(
        period=4.0,  # Wait 4 seconds before launching SLAM
        actions=[
            Node(
                package="slam_toolbox",
                executable="async_slam_toolbox_node",
                name="slam_toolbox",
                output="screen",
                parameters=[{
                    "use_sim_time": False,  # Now using system time
                    "odom_frame": "odom",
                    "base_frame": "base_footprint",
                    "map_frame": "map",
                    "scan_topic": "/scan",
                }]
            )
        ]
    )
    
    # RViz with delay - also using real time
    rviz_action = TimerAction(
        period=1.0,  # Wait 5 seconds before launching RViz
        actions=[
            Node(
                package='rviz2', 
                executable='rviz2', 
                name='rviz2', 
                output='screen',
                parameters=[{'use_sim_time': False}],  # Use real time
                arguments=['-d', LaunchConfiguration('rviz_config_file')]
            )
        ]
    )
    
    return LaunchDescription([
        rosbag_file,
        playback_rate,
        rviz_config_file,
        rosbag_play,
        transforms_action,
        odometry_action,
        slam_action,
        rviz_action,
    ])

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace  
  return LaunchDescription([
    transforms,
    rplidar,
  ])
  
  def generate_launch_description():
    # Arguments
    use_sim_time = DeclareLaunchArgument("use_sim_time", default_value="false")

    rviz_config_file = DeclareLaunchArgument("rviz_config_file", default_value="/home/biswash/workspace/map_rplidar/src/mapping_bringup/rviz/default_for_package.rviz", description="Path to the RViz configuration file")
    

    # RPLidar
    rplidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource('/home/biswash/workspace/map_rplidar/src/rplidar_ros/launch/rplidar_a1_launch.py')
    )

    # Static Transforms
    transforms = IncludeLaunchDescription(
        PythonLaunchDescriptionSource('/home/biswash/workspace/map_rplidar/src/transforms/launch/tf_setup_launch.py')
    )
    
    # Estimated Odometry 
    odometry = IncludeLaunchDescription(
        PythonLaunchDescriptionSource('/home/biswash/workspace/map_rplidar/src/rf2o_laser_odometry/launch/rf2o_laser_odometry.launch.py')
    )    

    # Slam Toolbox Node (real-time SLAM using RPLidar)
    slam_toolbox = Node(
        package="slam_toolbox",
        executable="async_slam_toolbox_node",
        name="slam_toolbox",
        output="screen",
        parameters=[{
            "use_sim_time": False,  # Use real-time clock
            "odom_frame": "odom",  # Define the odom frame
            "base_frame": "base_footprint",  # Define the base frame
            "map_frame": "map",  # Define the map frame
            "scan_topic": "/scan",  # RPLidar scan topic
        }]
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
        # Include transforms and RPLidar
        rviz_config_file,        
        rplidar,
        transforms,
        odometry,
        # Start Slam Toolbox
        slam_toolbox,
        rviz_action,
    ])

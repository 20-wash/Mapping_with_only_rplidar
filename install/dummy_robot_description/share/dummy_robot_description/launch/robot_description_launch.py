import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Declare the argument to pass the path to the URDF file
        DeclareLaunchArgument(
            'robot_description',
            default_value='$(find dummy_robot_description)/urdf/robot.urdf',
            description='Path to the URDF file'
        ),
        
        # Launch the robot_state_publisher node with the URDF or Xacro file
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': '$(find dummy_robot_description)/urdf/robot.xacro'}],
            output='screen'
        )
    ])

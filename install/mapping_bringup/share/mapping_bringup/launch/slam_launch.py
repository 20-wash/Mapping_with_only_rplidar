from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
          parameters=[
            # Custom config file in the 'mapping_bringup' package
            get_package_share_directory("mapping_bringup") + '/config/mapper_params_online_async_biswash.yaml',
            {"use_sim_time": False}  # Explicitly set sim time to false
          ],
          package='slam_toolbox',  # Package containing the SLAM nodes
          executable='async_slam_toolbox_node',  # Explicitly launching the async node
          name='slam_toolbox',  # Node name
          output='screen'  # Outputs logs to the screen
        )
    ])

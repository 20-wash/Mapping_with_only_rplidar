from setuptools import find_packages, setup

package_name = 'mapping_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/mapping_bringup/launch', ['launch/rp_lidar_launch.py']),
        ('share/mapping_bringup/launch', ['launch/bag_rp_lidar_slam_launch.py']), 
        ('share/mapping_bringup/launch', ['launch/rp_lidar_slam_launch.py']),          
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='biswash',
    maintainer_email='077bme014.biswash@pcampus.edu.np',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

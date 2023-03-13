from setuptools import setup
from glob import glob

package_name = 'simulation_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.*')), # copies launch files to the install/launch/ folder
        
        # copies configurations to the install/ folder so that they can be referred to from inside a launch file
        # without using absolute paths
        ('share/' + package_name, ['config/gazebo_topics.yaml', 'config/lidar_playground.sdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mcav',
    maintainer_email='mcav@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

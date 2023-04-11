from setuptools import setup
from glob import glob
import os

package_name = 'ros2_tutorial_Mouhid'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mouhidi216',
    maintainer_email='mouhidi216@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control = ros2_tutorial_Mouhid.control:main',
            'sense = ros2_tutorial_Mouhid.sense:main'
    
        ],
    },
)

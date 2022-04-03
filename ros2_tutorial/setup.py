from setuptools import setup

package_name = 'ros2_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='suryak',
    maintainer_email='skan0017@student.monash.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'task1 = ros2_tutorial.task1_node:main',
            'task2 = ros2_tutorial.task2_node:main',
            'task3 = ros2_tutorial.task3_node:main'
        ],
    },
)

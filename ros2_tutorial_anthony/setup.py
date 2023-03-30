from setuptools import setup

package_name = 'ros2_tutorial_anthony'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='newuser',
    maintainer_email='newuser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'control = ros2_tutorial_anthony.control:main',
                'sense = ros2_tutorial_anthony.sense:main',
        ],
    },
)

from setuptools import setup

package_name = 'ros2_tutorial_vedesh'

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
    maintainer='vedesh',
    maintainer_email='vedesh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'control = ros2_tutorial_vedesh.control:main',
        'sense = ros2_tutorial_vedesh.sense:main'
        ],
    },
)

from setuptools import setup

package_name = 'hello_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='laurie',
    maintainer_email='laurie@todo.todo',
    description='包含发送者和订阅者节点的 ROS2 包',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'ev_test_2_sender = hello_ros2.ev_test_2_sender:main',
            'ev_test_2_subscriber = hello_ros2.ev_test_2_subscriber:main',
        ],
    },
)


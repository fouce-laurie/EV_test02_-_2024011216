# publisher_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # 使用标准消息类型

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'chat_topic', 10)  # 创建话题
        self.timer = self.create_timer(1.0, self.publish_message)  # 定时发布
        self.counter = 0

    def publish_message(self):
        msg = String()
        msg.data = f"Hello, ROS2!"  # 消息内容
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")
        self.counter += 1

def main():
    rclpy.init()
    node = PublisherNode()
    rclpy.spin(node)  # 持续运行节点
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
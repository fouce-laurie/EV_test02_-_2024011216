#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入必要的ROS 2 Python库
import rclpy  # ROS 2 Python客户端库
from rclpy.node import Node  # 用于创建节点的基类
from std_msgs.msg import String  # 标准字符串消息类型

# 定义订阅者节点类，继承自Node
class SubscriberNode(Node):
    def __init__(self):
        # 调用父类构造函数，设置节点名称为'subscriber_node'
        super().__init__('subscriber_node')
        
        # 创建订阅者：
        # 1. 指定消息类型为String
        # 2. 订阅的话题名称为'chat_topic'
        # 3. 设置回调函数为listener_callback
        # 4. 设置队列长度为10（缓存的消息数量）
        self.subscription = self.create_subscription(
            String,
            'chat_topic',
            self.listener_callback,
            10
        )
        
        # 打印日志信息，表示订阅者已创建
        self.get_logger().info('Subscriber node started and listening to chat_topic...')

    # 定义消息回调函数
    def listener_callback(self, msg):
        # 当收到消息时，打印接收到的消息内容
        self.get_logger().info(f"2024011216 lu Yinhang")

# 主函数
def main():
    # 初始化ROS 2 Python客户端库
    rclpy.init()
    
    # 创建订阅者节点实例
    node = SubscriberNode()
    
    # 保持节点运行，等待消息到来
    # spin()会阻塞当前线程，直到节点被显式关闭
    rclpy.spin(node)
    
    # 节点关闭时，销毁节点
    node.destroy_node()
    
    # 关闭ROS 2 Python客户端库
    rclpy.shutdown()

# Python的标准入口点
if __name__ == '__main__':
    # 调用主函数
    main()
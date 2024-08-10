#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyboardSubscriber(Node):
    def __init__(self):
        super().__init__('keyboard_subscriber')
        print("listener is listening")
        self.subscription = self.create_subscription(
            String,
            'keyboard_input',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        if msg.data == 'w':
            self.get_logger().info('Move Forward')
        elif msg.data == 'a':
            self.get_logger().info('Move Left')
        elif msg.data == 's':
            self.get_logger().info('Move Backward')
        elif msg.data == 'd':
            self.get_logger().info('Move Right')
        else:
            self.get_logger().info('Invalid Key: %s' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    print("it has started")
    node = KeyboardSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


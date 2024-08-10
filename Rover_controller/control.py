#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher_ = self.create_publisher(String, 'keyboard_input', 10)
        self.timer = self.create_timer(0.1, self.run)
        self.input_key = None

    #ef timer_callback(self):
        

    def run(self):
            print("enter a character",end = '')
            self.input_key = input()
            print()
            if self.input_key:
                msg = String()
                msg.data = self.input_key
                self.publisher_.publish(msg)
                self.get_logger().info('Publishing: "%s"' % msg.data)
                self.input_key = None

def main(args=None):
    rclpy.init(args=args)            
    node = KeyboardPublisher()

    try:
        while True:
            node.run()
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


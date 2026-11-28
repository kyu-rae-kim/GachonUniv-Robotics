import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DirectionPublisher(Node):
    def __init__(self):
        super().__init__('get_dir')
        self.pub = self.create_publisher(String, '/direction', 10)
        self.timer = self.create_timer(0.1, self.publish_direction)

    def publish_direction(self):
        direction = input("Input Direction (w,s,a,d): ").lower()

        msg = String()
        msg.data = direction

        self.pub.publish(msg)
        self.get_logger().info(f'Published: {direction}')

def main():
    rclpy.init()
    node = DirectionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


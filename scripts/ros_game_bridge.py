#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed

class GameBridge():
    def __init__(self):
        rospy.init_node('game_bridge', anonymous=True)

        rospy.Subscriber("joint_angles", JointAnglesWithSpeed, self.handleJointAngles, queue_size=10)

        rospy.loginfo("Game Bridge running...")

        rospy.spin()

    def handleJointAngles(self, msg):
        rospy.loginfo("Game Bridge - Received a joint angle target")
        try:
            return
        except RuntimeError,e:
            rospy.logerr("Game Bridge - Exception caught:\n%s", e)

if __name__ == '__main__':
    try:
        game_bridge = GameBridge()
        rospy.loginfo("Game Bridge stopped")
    except rospy.ROSInterruptException:
        pass


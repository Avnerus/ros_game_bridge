#!/usr/bin/env python
import rospy
import websocket
from std_msgs.msg import String
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed


class GameBridge():
    def __init__(self):
        rospy.init_node('game_bridge', anonymous=True)

        rospy.Subscriber("joint_angles", JointAnglesWithSpeed, self.handleJointAngles, queue_size=10)

        rospy.loginfo("Game Bridge running...")

        websocket.enableTrace(True)
        self.ws = websocket.WebSocket()
        self.ws.connect("ws://127.0.0.1:8080/")
        self.ws.send("Hello, World")

        rospy.spin()

    def handleJointAngles(self, msg):
        rospy.loginfo("Game Bridge - Received a joint angle target")
        # Make a JSON
        json = "{'l':"+ str(msg.joint_angles[1]) + ",'r':" + str(msg.joint_angles[5]) + "}"
        self.ws.send(json)
        try:
            return
        except RuntimeError,e:
            rospy.logerr("Game Bridge - Exception caught:\n%s", e)

    def on_open(self, ws):
        return


if __name__ == '__main__':
    try:
        game_bridge = GameBridge()
        rospy.loginfo("Game Bridge stopped")
    except rospy.ROSInterruptException:
        pass


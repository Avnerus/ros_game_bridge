#!/usr/bin/env python
import websocket


websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8080/")
ws.send("Hello, World")



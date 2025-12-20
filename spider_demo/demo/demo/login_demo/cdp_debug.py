
import json

import websocket

webSocketDebuggerUrl = "ws://localhost:16666/devtools/page/7ED471273C76085673912DC46324ED63"

command = {
    'method': 'Debugger.evaluateOnCallFrame',
    'id': 1,
    'params': {
            "callFrameId": "54428407083467883.18.0",
            "expression": "deriveTokenSync('1')",
            "objectGroup": "console",
          "includeCommandLineAPI": True,
          "silent": False,
          "returnByValue": False,
          "generatePreview": True
}
}

connection = websocket.create_connection(webSocketDebuggerUrl)
connection.send(json.dumps(command))
print(json.loads(connection.recv()))

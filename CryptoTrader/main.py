import websocket
from library.my_functions import *


if __name__ == '__main__':
    ws=websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()



............from VisualRec import Server, WebServer, accounts_API

#accounts_API.create("", "1", "")


import threading

threading.Thread(target=WebServer.run).start()
Server.run()

#CheerCategory=9000\
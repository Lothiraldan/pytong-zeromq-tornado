class WebSocketHandler(websocket.WebSocketHandler):

    clients = {}

    def open(self, endpoints):
        for endpoint in endpoints:
            self.clients.setdefault(endpoint, set()).add(self)
        self.endpoints = endpoints

    def on_close(self):
        for endpoint in self.endpoints:
            self.clients.remove(self)

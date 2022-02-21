import socketserver, os, time, asyncio
import redis
r = redis.Redis(host='redis', port=6379)
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()

        r.set('foo', str(self.data, "utf-8")+' мой текст')
        print(r.get('foo'))

        # self.request.sendall(self.data.upper())
        self.request.sendall(bytes('foo', 'utf-8'))


def start_aserver():
    HOST, PORT = "0.0.0.0", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

if __name__ == "__main__":
    start_aserver()

# time.sleep(1000)
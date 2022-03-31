import subprocess, os, sys, time, asyncio, socket
import redis



data = "Some text from server A "
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect(('server', 9999))
	sock.sendall(bytes(data + "\n", "utf-8"))
	received = str(sock.recv(1024), "utf-8")
time.sleep(5)
print(f"Sent:     {data}")
print(f"Received: {received}")

r = redis.Redis(host='redis', port=6379)
rest = r.get(received)

print('test', rest)


# print('directory - ', os.listdir('/bpp'))
# time.sleep(1000)

# r = redis.Redis()
# r.mset({'soxwhite@gmail.com':['ghant', 'fb', 'insta']})
#
# s = r.get('soxwhite@gmail.com')
# print('redis', s)

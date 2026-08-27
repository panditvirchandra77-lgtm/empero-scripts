import subprocess, socket, ssl
host='token.sensenova.ai'
print('== DNS ==')
try:
    print(socket.getaddrinfo(host,443))
except Exception as e:
    print('dns fail', e)
print('== TCP connect 443 ==')
try:
    s=socket.create_connection((host,443),timeout=8)
    print('TCP OK', s.getpeername())
    s.close()
except Exception as e:
    print('TCP fail', str(e)[:80])

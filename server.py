import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 7788))
server.listen(1)

print("Waiting for client...")

conn, addr = server.accept()
print("Client connected:", addr)

while True:
    command = conn.recv(1024).decode().strip()

    if not command:
        break

    print("Command:", command)

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    output = result.stdout + result.stderr

    conn.send(output.encode())

conn.close()
server.close()
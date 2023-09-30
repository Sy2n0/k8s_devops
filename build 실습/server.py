import socket

with socket.socket() as s:
  s.bind(("0.0.0.0", 3000))
  s.listen()

  print("Server Started")
  conn, addr = s.accept()

  with conn:
    print("Connected by", addr)
    while True:
      data = conn.recv(1024)
      if not data: break
      conn.sendall(data)
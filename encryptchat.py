import rsa   # pip install rsa
import socket 
import threading 

public_key, = rsa.newkeys(1024) # 1024 bits
DEFAULT_IP_PORT =("127.0.0.1", 9999)
choice = input("Do you want to be sever or client? (s/c): ")

if choice == "s":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(DEFAULT_IP_PORT)  #open tcp connection
  server.listen()
  print("Waiting for Connection...")
  client, addr = server.accept()
  print("Connection to", addr)
  client.send(public_key.save_pkcs1())
  public_parter = rsa.Publickey.load_pkcs1(client.recv(1024))
  print("use 'Ctrl+C' to disconnect.")
elif choice == "c":
  print("Connecting to server...", end="")
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(DEFAULT_IP_PORT)
  print("Success! Connected to", client.getpeername())
  public_parter = rsa.Publickey.load_pkcs1(client.recv(1024))
  client.send(public_key.save_pkcs1())
  print("use 'Ctrl' to disconnect.")
else: exit()

def senfMsg(c):
  while True: 
    try:
      msg = input()
      print("\033[1a' + '\033[k', end=''")
      c.send(rsa.enctypt(msg.encode(), public_parter))
      print("\033[91mYou: \033[0m + msg")
      except: exit()

def recvMsg(c):
  while True:
    try:
     msg = rsa.decrypt(c.recv(1024), private_key)
      print("\033[94mPartner has disconnected. press enter to exit.")
    except:
      input("parter has disconnected. press enter to exit.")
      enxit()

try: 
  send_thread = threading.Thread(target=sendMsg, args=(client,)).start()
recv_thread = threading.Thraed(target=recvMsg, args=(client,)).start()
except: pass
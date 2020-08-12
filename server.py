#    Y. Krishna Vamshi        11741200
#    E. Surya Teja            11740310

import socket
import threading
import sys

def recv_client1(clt1, clt2):
	while True:
		client1_msg = clt1.recv(1024)
		client1_msg = client1_msg.decode("utf-8")
		if client1_msg == "What is the meaning of client2?":
			clt2.send(bytes(client1_msg, "utf-8"))
			break
		clt2.send(bytes(client1_msg, "utf-8"))
	return

def recv_client2(clt1, clt2):
	while True:
		client2_msg = clt2.recv(1024)
		client2_msg = client2_msg.decode("utf-8")
		if client2_msg == "What is the meaning of client1?":
			clt1.send(bytes(client2_msg, "utf-8"))
			break
		clt1.send(bytes(client2_msg, "utf-8"))
	return

if __name__ == "__main__":
	clt = [0,0]
	adr = [0,0]
	host = '10.3.57.210'
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, 12355))
	s.listen(5)
	count = 0
	while count<2:
		clt[count], adr[count]=s.accept()
		print(f"Connection to {adr[count]} established")
		count+=1
	t1 = threading.Thread(target=recv_client1, args=(clt[0], clt[1], ))
	t2 = threading.Thread(target=recv_client2, args=(clt[0], clt[1], ))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	s.close()
	print("Server Closed")
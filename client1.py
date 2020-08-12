#    Y. Krishna Vamshi        11741200
#    E. Surya Teja            11740310

import socket
import threading
import sys

def send():
	s_msg = input()
	while s_msg != "exit":
		if lock1 == 1:
			break
		s.send(bytes(s_msg, "utf-8"))
		s_msg = input()
	s.send(bytes("What is the meaning of client2?", "utf-8"))
	return

def receive():
	while True:
		r_msg = s.recv(1024)
		if r_msg.decode("utf-8") == "What is the meaning of client1?":
			print(" "*30, "\033[93m {}\033[00m" .format(r_msg.decode("utf-8")))
			s.send(bytes("What is the meaning of client2?", "utf-8"))
			lock1 = 1
			break
		else:
			print(" "*30, "\033[93m {}\033[00m" .format(r_msg.decode("utf-8")))
	return

if __name__ == "__main__":
	lock1 = 0
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '10.3.57.210'
	s.connect((host, 12355))
	print("Connected to "+host,"\n")
	t1 = threading.Thread(target=send)
	t2 = threading.Thread(target=receive)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	s.close()
	print("Chat Ended")
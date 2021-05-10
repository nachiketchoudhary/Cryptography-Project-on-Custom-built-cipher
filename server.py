import socket

message=input("Please enter your message ")
key = "abcklmnopqr0123456789 !@defghij#$%^stuvwxyz&*|"
val = key[:: -1]

encrypter = dict(zip(key, val))

message = "".join([encrypter[words] for words in message.lower()])
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3213))

s.listen(5)

while True:
   clt,adr= s.accept()

   clt.send(bytes(message, "utf-8"))


#msg = input("Please enter your message ")

#key = "abcdefghijklmnopqrstuvwxyz0123456789 !"

#val  = key[:: -1]

#e_msg = dict(zip(key , val))

#print(e_msg)

#enc_msg = "".join([e_msg[words] for words in msg.lower()])

#print((enc_msg))

#decrypter = dict(zip(val , key))

#dec_msg = "".join([e_msg[words] for words in enc_msg.lower()])

#print(dec_msg)
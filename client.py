import socket

dec_key = input("Give the encryption key ")

if len(dec_key) == 46:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((socket.gethostname(),3213 ))

    message = s.recv(1000)
    message =message.decode("utf-8")

    val = dec_key[:: -1]

    decrypter = dict(zip(val, dec_key))

    message = "".join([decrypter[words] for words in message.lower()])

    print(message)
else:
    print("Sorry, you are not authorised to view this message. ")